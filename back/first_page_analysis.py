import asyncio
import json
import requests
from bs4 import BeautifulSoup
import aiohttp
import re


async def get_channel_data(channel_name):
    '''
    :param channel_name: имя канала you_tube надо подставить вот сюда  'https://www.youtube.com/@{channel_name}/videos'
    :return:
    '''
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
    proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'

    async with aiohttp.ClientSession() as session:
        async with session.get(url=f'https://www.youtube.com/@{channel_name}/videos', headers=headers,
                               proxy=proxy_url) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'lxml')
            scripts = soup.find_all('script')
            for script in scripts:
                if 'ytInitialData' in script.text:
                    json_str = script.text
                    break
            if json_str is None:
                raise ValueError("ytInitialData not found in the page")

            json_str = json_str.split('var ytInitialData =')[1]
            json_str = json_str.rsplit('};', 1)[0] + '}'
            data = json.loads(json_str)

    return data


def find_keywords_in_page(data):
    # title = data['microformat']['microformatDataRenderer']['title']
    # channel_id = data['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][0]['text']
    # videos_count = data['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']
    # subscr_count = data['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']
    try:
        keywords_from_meta = data['metadata']['channelMetadataRenderer']['keywords']

        keywords_list = re.findall(r'"(.*?)"', keywords_from_meta)
        return keywords_list
    except:
        return None


def get_value_by_path(data, path):
    """Вспомогательная функция для извлечения значения из словаря по заданному пути."""
    for key in path:
        if isinstance(data, dict):
            data = data.get(key)
        elif isinstance(data, list):
            data = data[int(key)]
        else:
            return None
    return data


def find_continuation_token(input_dict, target_key):
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


def find_video_titles(data, max_titles=5):
    """Функция для извлечения заголовков видео из данных JSON."""
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
                # print(f"Title {i + 1}: {title}")
            if len(titles) >= max_titles:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    return titles


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

    video_titles = []
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post('https://www.youtube.com/youtubei/v1/browse', headers=headers,
                                    json=json_data) as response:
                data = await response.json()
                items = data['onResponseReceivedActions'][1]['reloadContinuationItemsCommand']['continuationItems']
                for item in items[:5]:
                    title = item['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
                    video_titles.append(title)
    except Exception as e:
        print(f"An error occurred: {e}")

    return video_titles


def general_func(channel_name):
    '''

    :param channel_name:  имя канала
    :return: возвращаем или ключевые слова или названия видео
    '''
    data = asyncio.run(get_channel_data(channel_name))
    keys = find_keywords_in_page(data)
    if len(keys) > 5:
        # логика для того что бы искать подходящие видео, использую ключевые слова канала
        # print('Есть ключевые слова на канале')
        return keys


    else:
        # ищу названия
        video_titles_first = find_video_titles(data, max_titles=10)
        # print(video_titles_first)
        tokens = find_continuation_token(input_dict=data, target_key='continuationCommand')
        popular_titles = []
        if len(tokens) > 1:
            token_to_popular = tokens[2]['token']
            # print('ищем популярные видео')
            popular_titles = asyncio.run(find_popular_video_titles(channel_name=channel_name, token=token_to_popular))
            # print(popular_titles)
        all_titles = video_titles_first + popular_titles
        return all_titles


channel_name1 = 'chestniyblog'
channel_name2 = 'nickiminaj'
channel_name3 = 'DontTellComedy'
channel_name4 = 'python228dlapypsikov'
channel_name5 = 'tkhirianov'
