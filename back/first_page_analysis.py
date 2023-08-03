import asyncio
import json
import requests
from bs4 import BeautifulSoup
import aiohttp
import re
from for_popular_video import find_popular_video_titles
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

# def main():
#     channel_url = "https://www.youtube.com/@chestniyblog/videos"
#     data = get_channel_data(channel_url)
#     tokens = list(find_continuation_tokens(data))
#     print("Continuation tokens:", tokens)
#     titles = find_video_titles(data)
#     print("Video titles:", titles)





def general_func(channel_name):
    '''

    :param channel_name:  имя канала
    :return:
    '''
    data = asyncio.run(get_channel_data(channel_name))
    keys = find_keywords_in_page(data)
    video_titles_first = find_video_titles(data, max_titles=10)
    tokens = find_continuation_token(input_dict=data, target_key='continuationCommand')
    # print(video_titles_first)
    # print(len(tokens))
    # print(type(tokens))
    if len(keys) > 5:
        # логика для того что бы искать подходящие видео, использую ключевые слова канала
        print('Есть ключевые слова на канале')
        print(keys)

    else:
        # ищу названия
        pass


channel_name1 = 'chestniyblog'
channel_name2 = 'nickiminaj'
channel_name3 = 'DontTellComedy'
channel_name4 = 'python228dlapypsikov'

general_func(channel_name1)