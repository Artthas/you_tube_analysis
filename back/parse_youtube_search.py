import requests
from bs4 import BeautifulSoup
import json
import aiohttp
import asyncio


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

    proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.youtube.com/results', params=params, headers=headers,
                               proxy=proxy_url) as response:
            print(response.url)
            return await response.text()


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
        videos_data.append(video_data)  # Добавляем словарь с данными о видео в список

    # Преобразуем список словарей в строку JSON с отступами в 4 пробела
    json_str = json.dumps(videos_data, indent=4, ensure_ascii=False)
    json_write(json_str)
    # Выводим строку JSON в консоль
    # print(json_str)
    return json_str


async def general_YT(search_query, quantity):
    content = await get_YT_search_html(search_query)
    json_data = return_json_dict(content)
    json_to_front = make_json(json_data, quantity)

    return json_to_front


def json_write(data):
    with open('videos_data.json', 'w') as f:
        json.dump(data, f, indent=4)
