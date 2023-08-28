import json
from bs4 import BeautifulSoup
import aiohttp
import re

from fastapi.exceptions import HTTPException
from aiohttp_socks import ProxyConnector
import asyncio
import logging
from you_tube_utils import *
logger = logging.getLogger(__name__)
from chat_gpt_api import *

class YouTubeScraper:
    def __init__(self, first_channel_name):
        # Инициализация атрибутов и настроек
        self.local_ip = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'
        self.ip_rotating = 'http://83.149.70.159:13012'
        self.proxy_url = self.local_ip  # сюда записать какой использую
        self.session = None


        self.dict_to_front = {}
        self.dict_channel_videos = {}

        self.data_with_new_video = None
        self.data_with_popular_video = None
        self.data_with_YT_search = None

        self.first_channel_name = first_channel_name
        self.continuation_token = None

        self.competitors_list = []

    async def create_session(self):

        connector = ProxyConnector.from_url(self.proxy_url)
        self.session = aiohttp.ClientSession(connector=connector)

    async def close_session(self):

        await self.session.close()

    async def get_page_with_new_videos_data(self, channel_name):
        """
        Получает данные первой страницы видео для указанного канала.
        :param channel_name: Имя канала на YouTube.
        :return: HTML-контент первой страницы видео.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
        }
        # url = f'https://www.youtube.com/c/{channel_name}/videos'
        MAX_RETRIES = 2
        DELAY_BETWEEN_RETRIES = 2  # задержка в 2 секунд
        for _ in range(MAX_RETRIES):
            try:
                async with self.session.get(f'https://www.youtube.com/@{channel_name}/videos', headers=headers) as response:
                    html = await response.text()
                    logger.info(f"Response status code get_channel_data: {response.status}")
                    # Проверка статуса ответа
                    if response.status == 404:
                        raise HTTPException(status_code=404, detail="Incorrect channel name")
                    elif response.status != 200:
                        raise HTTPException(status_code=response.status, detail="Failed to get data from YouTube")

                    # Парсинг HTML с использованием BeautifulSoup
                    soup = BeautifulSoup(html, 'lxml')
                    scripts = soup.find_all('script')
                    # Поиск скрипта, содержащего ytInitialData
                    for script in scripts:
                        if 'ytInitialData' in script.text:
                            json_str = script.text
                            break
                    if json_str is None:
                        raise ValueError("ytInitialData not found in the page")

                    json_str = json_str.split('var ytInitialData =')[1]
                    json_str = json_str.rsplit('};', 1)[0] + '}'
                    self.data_with_new_video = json.loads(json_str)
                    # with open('data.json', 'w', encoding='utf-8') as f:
                    #     json.dump(self.data_with_new_video, f, ensure_ascii=False, indent=4)
                    break
            except aiohttp.ClientProxyConnectionError:
                if _ < MAX_RETRIES - 1:  # Если это не последняя попытка
                    await asyncio.sleep(DELAY_BETWEEN_RETRIES)  # Добавляем задержку перед следующей попыткой
                else:
                    raise  # Если это была последняя попытка, выбрасываем исключение

    # Функции из first_page_analysis.py
    def page_with_new_videos_analysis(self):
        path_to_contents = [
            "contents", "twoColumnBrowseResultsRenderer", "tabs", 1, "tabRenderer",
            "content", "richGridRenderer", "contents"
        ]

        videos = []
        try:
            contents = get_value_by_path(self.data_with_new_video, path_to_contents)
            channel_name_path = ["contents", "twoColumnBrowseResultsRenderer", "tabs", 1, "tabRenderer", "endpoint",
                                 "browseEndpoint", "canonicalBaseUrl"]
            try:
                channel_name = get_value_by_path(self.data_with_new_video, channel_name_path).replace('/@', '')
            except:
                channel_name = 'none'
            # for i, content in enumerate(contents[0:-2]):
            for i, content in enumerate(contents):
                try:
                    title_path = ["richItemRenderer", "content", "videoRenderer", "title", "runs", 0, "text"]
                    url_path = ["richItemRenderer", "content", "videoRenderer", "navigationEndpoint", "commandMetadata",
                                "webCommandMetadata", "url"]
                    thumbnail_path = ["richItemRenderer", "content", "videoRenderer", "thumbnail", "thumbnails", 0, "url"]
                    view_count_path = ["richItemRenderer", "content", "videoRenderer", "viewCountText", "simpleText"]

                    title = get_value_by_path(content, title_path)
                    url = get_value_by_path(content, url_path)
                    thumbnail = get_value_by_path(content, thumbnail_path)
                    view_count = views_to_int(get_value_by_path(content, view_count_path))

                    if title and url and thumbnail and view_count:

                        video_info = {
                            "title": title,
                            "url": f"https://www.youtube.com/{url}",
                            "thumbnail": thumbnail,
                            "view_count": view_count
                        }
                        # print(title, url, view_count, thumbnail)
                        videos.append(video_info)
                except:
                    pass

            self.dict_channel_videos = {channel_name.lower(): {
                'all_new_videos': videos,  # исходный список видео
                'top_new_videos': sorted(videos, key=lambda x: x['view_count'], reverse=True)[:int(len(videos) * 0.2)]
                # топ 20% видео
            }}
        except Exception as e:
            print(f"An error occurred in first_page_analysis: {e}")


    async def get_data_from_page_with_popular_video_data(self, channel_name, token):
        logger.info(f'start find popular video in {channel_name}')
        headers = {
            'authority': 'www.youtube.com',
            'accept': '*/*',
            'accept-language': 'en',
            'content-type': 'application/json',
            'origin': 'https://www.youtube.com',
            'referer': f'https://www.youtube.com/@{channel_name}/videos',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-youtube-client-name': '1',
            'x-youtube-client-version': '2.20230725.07.00',
        }

        json_data = {
            'context': {
                'client': {
                    'hl': 'en',
                    'visitorData': 'Cgtjdk9QbFZtZ2M4QSit9oqmBg%3D%3D',
                    'userAgent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36,gzip(gfe)',
                    'clientName': 'WEB',
                    'clientVersion': '2.20230725.07.00',
                    'osName': 'X11',
                    'osVersion': '',
                    'originalUrl': f'https://www.youtube.com/@{channel_name}/videos',
                    'screenPixelDensity': 1,
                    'platform': 'DESKTOP',
                    'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                },
            },
            'continuation': f'{token}',
        }

        MAX_RETRIES = 2
        DELAY_BETWEEN_RETRIES = 2  # задержка в 2 секунд

        for _ in range(MAX_RETRIES):
            try:

                async with self.session.post('https://www.youtube.com/youtubei/v1/browse', headers=headers,
                                        json=json_data) as response:

                    data = await response.json()
                    # print(data)
                    items = data['onResponseReceivedActions'][1]['reloadContinuationItemsCommand']['continuationItems']
                    videos = []
                    for item in items:
                        if 'richItemRenderer' in item:  # Проверка на наличие ключа 'richItemRenderer'
                            title = item['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
                            url_path = ["richItemRenderer", "content", "videoRenderer", "navigationEndpoint",
                                        "commandMetadata", "webCommandMetadata", "url"]
                            thumbnail_path = ["richItemRenderer", "content", "videoRenderer", "thumbnail", "thumbnails",
                                              0, "url"]
                            view_count_path = ["richItemRenderer", "content", "videoRenderer", "shortViewCountText",
                                               "accessibility", "accessibilityData", "label"]

                            url = get_value_by_path(item, url_path)
                            thumbnail = get_value_by_path(item, thumbnail_path)
                            view_count_string = get_value_by_path(item, view_count_path)
                            view_count = views_to_int(view_count_string)

                            video_info = {
                                "title": title,
                                "url": f"https://www.youtube.com/{url}",
                                "thumbnail": thumbnail,
                                "view_count": view_count
                            }
                            videos.append(video_info)


                    self.dict_channel_videos[channel_name.lower()]['all_popular_videos'] = videos
                    self.dict_channel_videos[channel_name.lower()]['top_popular_videos'] = sorted(videos,
                                                                                                  key=lambda x: x[
                                                                                                      'view_count'],
                                                                                                  reverse=True)[
                                                                                           :int(len(videos) * 0.2)]
            except:
                logger.info(f"Response status code find_popular_video_titles: {response.status}")
                logger.info("An error occurred in find_popular_video_titles")
                if _ < MAX_RETRIES - 1:  # Если это не последняя попытка
                    await asyncio.sleep(DELAY_BETWEEN_RETRIES)  # Добавляем задержку перед следующей попыткой
                else:
                    raise  # Если это была последняя попытка, выбрасываем исключение


    async def get_YT_search_html(self, search_query):
        headers = {
            'authority': 'www.youtube.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }

        params = {
            'search_query': search_query,
            # 'sp': 'CAMSAggF', # max views
            'sp': 'EgIIBQ%3D%3D'  # relevant
        }

        MAX_RETRIES = 2
        DELAY_BETWEEN_RETRIES = 2  # задержка в 2 секунд
        for _ in range(MAX_RETRIES):
            try:
                async with self.session.get('https://www.youtube.com/results', params=params, headers=headers) as response:
                    logger.info(f"Response status code get_YT_search_html: {response.status}")
                    print(response.url)
                    content = await response.text()
                    json_data = return_json_dict(content)
                    you_tube_search = make_json(json_data, quantity=20)
                    self.data_with_YT_search = you_tube_search
                    for item in self.data_with_YT_search:
                        comp_name = item['channel_url'].split('/@')[-1]
                        if comp_name not in self.competitors_list:
                            self.competitors_list.append(comp_name)
                    break

            except Exception as e:
                print(f"An error occurred in get_YT_search_html: {e}")
                if _ < MAX_RETRIES - 1:  # Если это не последняя попытка
                    await asyncio.sleep(DELAY_BETWEEN_RETRIES)  # Добавляем задержку перед следующей попыткой
                else:
                    raise  # Если это была последняя попытка, выбрасываем исключение
    async def parse_concurence(self):

        if len(self.competitors_list) > 0:
            for competitor in self.competitors_list:
                competitor_name = competitor.lower()
                self.create_session()

        pass

    # Функции из parse_youtube_search.py


    def return_json_dict(self, content):
        # Ваш код
        pass

    def extract_video_data(self, json_data, index):
        # Ваш код
        pass

    def get_nested(self, data, path):
        # Ваш код
        pass

    def make_json(self, json_data, quantity):
        # Ваш код
        pass

    async def general_YT(self, search_query, quantity, proxy_url):
        connector = ProxyConnector.from_url(proxy_url)
        async with aiohttp.ClientSession(connector=connector) as session:
            content = await self.get_YT_search_html(search_query, session)
            json_data = self.return_json_dict(content)
            return self.make_json(json_data, quantity)

    # Функции из utils.py
    def some_util_function(self):
        # Ваш код
        pass

    # Функции из for_popular_video.py
    def for_popular_video(self):
        # Ваш код
        pass



# DaFuqBoom хрень канал
# thefugitiveofficial   rapdailyofficial

async def general_func():
    channel_name = 'thefugitiveofficial'.lower()
    yt_scrap = YouTubeScraper(first_channel_name=channel_name)
    await yt_scrap.create_session()
    await yt_scrap.get_page_with_new_videos_data(channel_name=yt_scrap.first_channel_name)
    yt_scrap.page_with_new_videos_analysis()

    tokens = find_continuation_token(yt_scrap.data_with_new_video, target_key='continuationCommand')
    if len(tokens) > 1:
        yt_scrap.continuation_token = tokens[2]['token']
    if yt_scrap.continuation_token:
        await yt_scrap.get_data_from_page_with_popular_video_data(channel_name=channel_name, token=yt_scrap.continuation_token)


    d = yt_scrap.dict_channel_videos
    # await yt_scrap.close_session()

    yt_scrap.dict_channel_videos[channel_name]['description'] = await get_description(yt_scrap.dict_channel_videos[channel_name])

    # только для главного канала
    yt_scrap.dict_channel_videos[channel_name]['key_words'] = await get_keywords(yt_scrap.dict_channel_videos[channel_name])
    print('YA BABY main file here')
    # print(yt_scrap.dict_channel_videos[channel_name]['description'])
    # print(yt_scrap.dict_channel_videos[channel_name]['key_words'])

    await yt_scrap.get_YT_search_html(yt_scrap.dict_channel_videos[channel_name]['key_words'])
    dict_YT = yt_scrap.data_with_YT_search
    # print(yt_scrap.data_with_popular_video)
    print(json.dumps(dict_YT, indent=4))
    print(yt_scrap.competitors_list)
    await yt_scrap.close_session()

# Запускаем асинхронный код
asyncio.run(general_func())
# https://www.youtube.com//watch?v=qmvDrQoLz8g