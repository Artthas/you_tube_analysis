import json
import requests
from bs4 import BeautifulSoup
import re

channel_name1 = 'chestniyblog'
channel_name2 = 'nickiminaj'
channel_name3 = 'DontTellComedy'
url = 'https://www.youtube.com/@chestniyblog/videos'
url2 = 'https://www.youtube.com/@nickiminaj/videos'
url3 = 'https://www.youtube.com/@DontTellComedy/videos'


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

proxies = {
    'http': proxy_url,
    'https': proxy_url,
}

response = requests.get(f'https://www.youtube.com/@{channel_name3}/videos', headers=headers, proxies=proxies)


# with open('page.html', 'a') as f:
#     f.write(response.text)nickiminaj

# with open('page.html', 'r') as f:
#     soup = BeautifulSoup(f.read(), 'lxml')



"""
responseContext
contents
header
metadata
trackingParams
topbar
microformat
/microformat/microformatDataRenderer/title
/metadata/channelMetadataRenderer/keywords
/metadata/channelMetadataRenderer/ownerUrls
/header/c4TabbedHeaderRenderer/channelHandleText/runs/0/text
/header/c4TabbedHeaderRenderer/videosCountText/runs/0/text
/header/c4TabbedHeaderRenderer/subscriberCountText/accessibility/accessibilityData/label
/header/c4TabbedHeaderRenderer/subscriberCountText/simpleText

/contents/twoColumnBrowseResultsRenderer/tabs/1/tabRenderer/content/richGridRenderer/contents/0/richItemRenderer/content/videoRenderer/title/runs/0/text
/contents/twoColumnBrowseResultsRenderer/tabs/1/tabRenderer/content/richGridRenderer/contents/1/richItemRenderer/content/videoRenderer/title/runs/0/text
"""
soup = BeautifulSoup(response.text, 'lxml')
scripts = soup.find_all('script')
for script in scripts:
    if 'ytInitialData' in script.text:
        json_str = script.text
        break
json_str = json_str.split('var ytInitialData =')[1]
json_str = json_str.rsplit('};', 1)[0] + '}'
# print(json_str)
# json_str = json_str.split(';</script>')[0]
data = json.loads(json_str)
# print(json.dumps(data, indent=4))
# with open('my_json1.json', 'a', encoding='utf-8') as j1:
#     j1.write(json.dumps(data, indent=4, ensure_ascii=False))

print(data.keys())
title = data['microformat']['microformatDataRenderer']['title']
keywords_from_meta = data['metadata']['channelMetadataRenderer']['keywords']
channel_id = data['header']['c4TabbedHeaderRenderer']['channelHandleText']['runs'][0]['text']
videos_count = data['header']['c4TabbedHeaderRenderer']['videosCountText']['runs'][0]['text']
subscr_count = data['header']['c4TabbedHeaderRenderer']['subscriberCountText']['simpleText']

print(title)
print(channel_id)
print(subscr_count)
print(videos_count)
print(keywords_from_meta)
print(type(keywords_from_meta))
keywords_list = re.findall(r'"(.*?)"', keywords_from_meta)
print(keywords_list)
##################################
# looking for continuation token #
##################################

"""
/contents/twoColumnBrowseResultsRenderer/tabs/1/tabRenderer/content/richGridRenderer/contents/30/continuationItemRenderer/continuationEndpoint/continuationCommand/token

"""

def find_key(input_dict, target_key):
    # if target_key in input_dict:
    #     yield input_dict[target_key]
    # elif isinstance(input_dict, dict):
    #     for k, v in input_dict.items():
    #         if isinstance(v, (dict, list)):
    #             yield from find_key(v, target_key)
    # elif isinstance(input_dict, list):
    #     for item in input_dict:
    #         yield from find_key(item, target_key)
    found_values = []
    if target_key in input_dict:
        found_values.append(input_dict[target_key])
    elif isinstance(input_dict, dict):
        for k, v in input_dict.items():
            if isinstance(v, (dict, list)):
                found_values.extend(find_key(v, target_key))
    elif isinstance(input_dict, list):
        for item in input_dict:
            found_values.extend(find_key(item, target_key))
    return found_values


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
                print(f"Video {i+1}: {title}")  # печатаем порядковый номер и заголовок видео

                titles.append(title)
            if len(titles) >= max_titles:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    return titles


a = find_key(input_dict=data, target_key='continuationCommand')
print(len(a))
# for i in a:
#     print(i['token'])




titles = find_video_titles(data)
print(titles)