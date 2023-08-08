import requests
from bs4 import BeautifulSoup
import json
import aiohttp
import asyncio
from aiohttp_socks import ProxyConnector
import logging
logger = logging.getLogger(__name__)

async def get_YT_search_html(search_query):
    headers = {
        'authority': 'www.youtube.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    params = {
        'search_query': search_query,
        'sp': 'CAMSAggF',
    }

    proxy_url_rotate = 'http://83.149.70.159:13012'


    MAX_RETRIES = 20
    DELAY_BETWEEN_RETRIES = 5  # задержка в 5 секунд

    for _ in range(MAX_RETRIES):
        try:
            # Создание соединителя для прокси
            connector = ProxyConnector.from_url(proxy_url_rotate)
            # Создание асинхронной сессии
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get('https://www.youtube.com/results', params=params, headers=headers) as response:
                    logger.info(f"Response status code get_YT_search_html: {response.status}")
                    print(response.url)
                    return await response.text()  # Возвращаем результат после успешного выполнения запроса

        except Exception as e:
            print(f"An error occurred in get_YT_search_html: {e}")
            if _ < MAX_RETRIES - 1:  # Если это не последняя попытка
                await asyncio.sleep(DELAY_BETWEEN_RETRIES)  # Добавляем задержку перед следующей попыткой
            else:
                raise  # Если это была последняя попытка, выбрасываем исключение



def return_json_dict(content):
    soup = BeautifulSoup(content, 'lxml')
    scripts = soup.find_all('script')

    for script in scripts:
        if 'ytInitialData' in script.text:
            json_str = script.text
            break
    json_str = json_str.split('var ytInitialData =')[1]
    json_str = json_str.rsplit('};', 1)[0] + '}'
    json_data = json.loads(json_str)
    print(type(json_data))
    return json_data


def extract_video_data(json_data, index):
    base_path = ['contents', 'twoColumnSearchResultsRenderer', 'primaryContents', 'sectionListRenderer', 'contents', 0,
                 'itemSectionRenderer', 'contents', index, 'videoRenderer']
    vid_base_url = 'https://www.youtube.com'
    video_url = get_nested(json_data,
                           base_path + ['navigationEndpoint', 'commandMetadata', 'webCommandMetadata', 'url'])
    channel_url = get_nested(json_data,
                             base_path + ['longBylineText', 'runs', 0, 'navigationEndpoint', 'commandMetadata',
                                          'webCommandMetadata', 'url'])
    video_data = {
        'video_url': vid_base_url + video_url if video_url else video_url,
        'thumbnail_360x202': get_nested(json_data, base_path + ['thumbnail', 'thumbnails', 0, 'url']),
        'thumbnail_720x404': get_nested(json_data, base_path + ['thumbnail', 'thumbnails', 1, 'url']),
        'title_text': get_nested(json_data, base_path + ['title', 'runs', 0, 'text']),
        'title_label': get_nested(json_data, base_path + ['title', 'accessibility', 'accessibilityData', 'label']),
        'channel_url': vid_base_url + channel_url if channel_url else channel_url,
        'channel_text': get_nested(json_data, base_path + ['longBylineText', 'runs', 0, 'text']),
        'published_time': get_nested(json_data, base_path + ['publishedTimeText', 'simpleText']),
        'video_length': get_nested(json_data, base_path + ['lengthText', 'simpleText']),
        'view_count': get_nested(json_data, base_path + ['viewCountText', 'simpleText']),
    }

    return video_data


def get_nested(data, path):
    for key in path:
        if isinstance(data, dict):
            data = data.get(key)
        elif isinstance(data, list):
            try:
                key = int(key)
                data = data[key]
            except (ValueError, IndexError):
                return None
        else:
            return None
    return data



def make_json(json_data, quantity):
    videos_data = []
    for i in range(quantity):
        video_data = extract_video_data(json_data, i)
        # Если хотя бы одно значения в словаре равны None, пропускаем его
        if not any(value is None for value in video_data.values()):
            videos_data.append(video_data)  # Добавляем словарь с данными о видео в список

    return videos_data

async def general_YT(search_query, quantity):
    retry_count = 0
    while retry_count < 20:  # Повторяем до 20 раз
        try:
            content = await get_YT_search_html(search_query)
            json_data = return_json_dict(content)
            json_to_front = make_json(json_data, quantity)
            return json_to_front
        except aiohttp.ClientProxyConnectionError:
            retry_count += 1
            await asyncio.sleep(5)  # Задержка 5 секунд перед следующей попыткой


def json_write(data):
    with open('videos_data.json', 'w') as f:
        json.dump(data, f, indent=4)
