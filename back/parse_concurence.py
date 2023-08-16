import json
from bs4 import BeautifulSoup
import aiohttp
import re
from chat_gpt_api import get_keywords
from fastapi.exceptions import HTTPException
from aiohttp_socks import ProxyConnector
import asyncio
import logging

logger = logging.getLogger(__name__)


async def get_channel_data(channel_name):
    """
    Асинхронная функция для получения данных о видео на YouTube по имени канала.

    :param channel_name: Имя канала на YouTube.
    :return: Словарь с данными о видео на канале.
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
    # Прокси-сервер для запроса
    proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'
    proxy_url_rotate = 'http://83.149.70.159:13012'
    # Создание соединителя для прокси
    connector = ProxyConnector.from_url(proxy_url)
    MAX_RETRIES = 20
    DELAY_BETWEEN_RETRIES = 5  # задержка в 5 секунд
    for _ in range(MAX_RETRIES):
        try:
            # Создание асинхронной сессии
            async with aiohttp.ClientSession(connector=connector) as session:
                # Отправка GET-запроса к YouTube
                async with session.get(url=f'https://www.youtube.com/@{channel_name}/videos',
                                       headers=headers) as response:
                    # Получение HTML-ответа
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
                    data = json.loads(json_str)
                    return data  # Если все прошло успешно, выходим из цикла и возвращаем данные
        except aiohttp.ClientProxyConnectionError:
            if _ < MAX_RETRIES - 1:  # Если это не последняя попытка
                await asyncio.sleep(DELAY_BETWEEN_RETRIES)  # Добавляем задержку перед следующей попыткой
            else:
                raise  # Если это была последняя попытка, выбрасываем исключение


def find_keywords_in_page(data):
    try:
        keywords_from_meta = data['metadata']['channelMetadataRenderer']['keywords']

        keywords_list = re.findall(r'"(.*?)"', keywords_from_meta)
        return keywords_list
    except:
        return None


def get_value_by_path(data, path):
    """
    Получает значение из словаря или списка, следуя указанному пути.

    :param data: Словарь или список, из которого нужно извлечь значение.
    :param path: Список ключей или индексов, указывающих путь к значению.
    :return: Значение, найденное по указанному пути, или None, если путь не существует.
    """
    for key in path:
        if isinstance(data, dict):
            data = data.get(key)
        elif isinstance(data, list):
            data = data[int(key)]
        else:
            return None
    return data


def find_continuation_token(input_dict, target_key):
    """
    Рекурсивно ищет все значения в словаре по указанному ключу.

    :param input_dict: Словарь для поиска.
    :param target_key: Ключ, который нужно найти.
    :return: Список всех найденных значений.
    """
    found_values = []
    if target_key in input_dict:
        found_values.append(input_dict[target_key])
    elif isinstance(input_dict, dict):
        for k, v in input_dict.items():
            if isinstance(v, (dict, list)):
                found_values.extend(find_continuation_token(v, target_key))
    elif isinstance(input_dict, list):
        for item in input_dict:
            found_values.extend(find_continuation_token(item, target_key))
    return found_values


def find_video_titles(data, max_titles=20):
    """
    Ищет названия видео на странице канала YouTube.

    :param data: Словарь с данными страницы.
    :param max_titles: Максимальное количество названий, которые нужно вернуть.
    :return: Список названий видео.
    """
    path_to_titles = [
        "contents", "twoColumnBrowseResultsRenderer", "tabs", 1, "tabRenderer",
        "content", "richGridRenderer", "contents"
    ]

    titles = []
    try:
        contents = get_value_by_path(data, path_to_titles)
        for i, content in enumerate(contents):
            title_path = ["richItemRenderer", "content", "videoRenderer", "title", "runs", 0, "text"]
            title = get_value_by_path(content, title_path)
            if title:
                titles.append(title)
            if len(titles) >= max_titles:
                break
    except Exception as e:
        print(f"An error occurred find_video_titles: {e}")
    return titles


# функия для получения сслыки на фото, сслыки на видео и названий видео
def find_video_titles_url_thumb(data, max_titles=20):
    """
    Ищет названия видео, ссылки на видео и ссылки на изображения на странице канала YouTube.

    :param data: Словарь с данными страницы.
    :param max_titles: Максимальное количество названий, которые нужно вернуть.
    :return: Список словарей с информацией о видео.
    """
    path_to_contents = [
        "contents", "twoColumnBrowseResultsRenderer", "tabs", 1, "tabRenderer",
        "content", "richGridRenderer", "contents"
    ]

    videos = []
    try:
        contents = get_value_by_path(data, path_to_contents)
        for i, content in enumerate(contents):
            title_path = ["richItemRenderer", "content", "videoRenderer", "title", "runs", 0, "text"]
            url_path = ["richItemRenderer", "content", "videoRenderer", "navigationEndpoint", "commandMetadata",
                        "webCommandMetadata", "url"]
            thumbnail_path = ["richItemRenderer", "content", "videoRenderer", "thumbnail", "thumbnails", 0, "url"]

            title = get_value_by_path(content, title_path)
            url = get_value_by_path(content, url_path)
            thumbnail = get_value_by_path(content, thumbnail_path)

            if title and url and thumbnail:
                video_info = {
                    "title": title,
                    "url": f"https://www.youtube.com/{url}",
                    "thumbnail": thumbnail
                }
                videos.append(video_info)

            if len(videos) >= max_titles:
                break
    except Exception as e:
        print(f"An error occurred in find_video_titles: {e}")
    return videos


async def find_popular_video_titles(channel_name, token):
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
    proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'
    video_titles = []
    videos = []
    proxy_url_rotate = 'http://83.149.70.159:13012'

    MAX_RETRIES = 20
    DELAY_BETWEEN_RETRIES = 5  # задержка в 5 секунд

    for _ in range(MAX_RETRIES):
        try:
            # Создание соединителя для прокси
            connector = ProxyConnector.from_url(proxy_url)
            # Создание асинхронной сессии
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.post('https://www.youtube.com/youtubei/v1/browse', headers=headers,
                                        json=json_data) as response:

                    data = await response.json()

                    logger.info(f"Response status code find_popular_video_titles: {response.status}")

                    items = data['onResponseReceivedActions'][1]['reloadContinuationItemsCommand']['continuationItems']
                    for item in items:
                        if 'richItemRenderer' in item:  # Проверка на наличие ключа 'richItemRenderer'
                            title = item['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
                            url_path = ["richItemRenderer", "content", "videoRenderer", "navigationEndpoint",
                                        "commandMetadata", "webCommandMetadata", "url"]
                            thumbnail_path = ["richItemRenderer", "content", "videoRenderer", "thumbnail", "thumbnails",
                                              0, "url"]

                            url = get_value_by_path(item, url_path)
                            thumbnail = get_value_by_path(item, thumbnail_path)
                            video_info = {
                                "title": title,
                                "url": f"https://www.youtube.com/{url}",
                                "thumbnail": thumbnail
                            }
                            videos.append(video_info)
                            video_titles.append(title)
                    return {'video_titles': video_titles,
                            'videos': videos}  # Возвращаем video_titles после успешного выполнения запроса

        except Exception as e:
            print(f"An error occurred in find_popular_video_titles: {e}")
            if _ < MAX_RETRIES - 1:  # Если это не последняя попытка
                await asyncio.sleep(DELAY_BETWEEN_RETRIES)  # Добавляем задержку перед следующей попыткой
            else:

                raise  # Если это была последняя попытка, выбрасываем исключение
async def general_func_concurence(channel_name):
    retry_count = 0
    while retry_count < 20:  # Повторяем до 20 раз
        try:
            data = await get_channel_data(channel_name)
            video_titles_first = find_video_titles(data, max_titles=10)
            tokens = find_continuation_token(input_dict=data, target_key='continuationCommand')
            popular_titles = []
            if len(tokens) > 1:
                token_to_popular = tokens[2]['token']
                popular_titles = await find_popular_video_titles(channel_name=channel_name, token=token_to_popular)


            # что бы было не слишком много заголовков. И в идеале только популырные
            if len(popular_titles['video_titles']) > 1:
                all_titles = video_titles_first[:5] + popular_titles['video_titles'][:5]
            else:
                all_titles = video_titles_first[:7]

            return {channel_name: all_titles}
        except aiohttp.ClientProxyConnectionError:
            retry_count += 1
            await asyncio.sleep(5)  # Задержка 5 секунд перед следующей попыткой


# courtinvestigation
# concurence_channals = ['AETV', 'CBSNews', 'thv11', 'LawyerYouKnow', 'RoomforDiscussionUva', 'LawAndCrime', 'NBCNews',
#                        'BanijayCrime', 'CBCNews']

# channel_name = 'AETV'
# # Получение ключевых слов для поиска видео по имени канала
# dict_with_titles_competitors = asyncio.run(general_func_concurence(channel_name))
#
# print(dict_with_titles_competitors)


async def process_channel(channel_name):
    return await general_func_concurence(channel_name)


async def func_for_titles_competitors(selected_competitors):
    if not selected_competitors:
        return []
    tasks = [process_channel(channel_name) for channel_name in selected_competitors]
    results = await asyncio.gather(*tasks)
    return results

#
# selected_competitors = ['AETV', 'CBSNews', 'thv11', 'LawyerYouKnow', 'RoomforDiscussionUva']
#
# dict_with_titles_competitors = asyncio.run(func_for_titles_competitors(selected_competitors))
#
#
# try:
#     print(json.dumps(dict_with_titles_competitors, indent=4))
# except:
#     print(dict_with_titles_competitors)
