import requests
from bs4 import BeautifulSoup
import json

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = {
    # 'search_query': """Stand-Up Comedy | stand up comedy | stand up | comedians stand up comedy | standup comedy | stand-up comedy | dont tell comedy | don't tell comedy | mark smalls | michael longfellow | secret comedy shows | backyard comedy shows | funny jokes | comedy specials | best comedians""",
    'search_query': 'какой телефон лучше | тест камер | dj feel | опыт использования | русский russian | честный блог | redmi note 8 pro | iphone 11 pro | iphone se | купить смартфон | какой смартфон купить | честный блог | s22 ultra | poco x3 pro | iphone 14 pro | xiaomi 12s ultra | pixel 7 pro | pixel 6 pro | самсунг с22 | пиксель 7 про',
    # 'search_query': 'Nicki Minaj | young money | cash money | republic records | lil wayne | Pink Friday | Super Bass | Anaconda Nicki | city girls | kash doll | megan thee stallion',
    # 'search_query': 'Информатика | лекция | КЕГЭ | Фоксфорд | Python 3 | Алгоритмы | практика программирования | кодирование | ориентированный граф',
    'sp': 'CAMSAggF',
    # 'sp': 'CAESBAgFEAE%3D',
    # 'sp': 'CAMSBAgFEAE%3D'
}

"""
ссылка на видео  строка 171
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/navigationEndpoint/commandMetadata/webCommandMetadata/url

ссылка на начальную картинку 360 на 202  строка 108
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/thumbnail/thumbnails/0/url

ссылка на начальную картинку 720 на 404  строка 108
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/thumbnail/thumbnails/1/url

title text строка 122
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/title/runs/0/text

title label строка 127
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/title/accessibility/accessibilityData/label


ссылка на канал строка 139
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/longBylineText/runs/0/navigationEndpoint/commandMetadata/webCommandMetadata/url

текст канала  строка 134
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/longBylineText/runs/0/text


publishedTimeText  строка 154
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/publishedTimeText/simpleText

длинна  строка 162
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/lengthText/simpleText

viewCountText  строка 165
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/videoRenderer/viewCountText/simpleText


/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/0/
/contents/twoColumnSearchResultsRenderer/primaryContents/sectionListRenderer/contents/0/itemSectionRenderer/contents/1/
"""

response = requests.get('https://www.youtube.com/results', params=params, headers=headers)
print(response.url)

# with open('result11.html', 'a') as f:
#     f.write(response.text)
# print(response.text)

# with open('result11.html', 'r') as f:
#     content = f.read()
#
soup = BeautifulSoup(response.text, 'lxml')
scripts = soup.find_all('script')

for script in scripts:
    if 'ytInitialData' in script.text:
        json_str = script.text
        break
json_str = json_str.split('var ytInitialData =')[1]
json_str = json_str.rsplit('};', 1)[0] + '}'
json_data = json.loads(json_str)
print(type(json_data))
#
# with open('res.json', 'a') as f:
#     json.dump(data, f, indent=4)

# with open('res.json', 'r') as f:
#     json_data = json.load(f)


def extract_video_data(json_data, index):
    base_path = ['contents', 'twoColumnSearchResultsRenderer', 'primaryContents', 'sectionListRenderer', 'contents', 0, 'itemSectionRenderer', 'contents', index, 'videoRenderer']
    vid_base_url = 'https://www.youtube.com'
    video_data = {
        'video_url': get_nested(json_data, base_path + ['navigationEndpoint', 'commandMetadata', 'webCommandMetadata', 'url']),
        'thumbnail_360x202': get_nested(json_data, base_path + ['thumbnail', 'thumbnails', 0, 'url']),
        'thumbnail_720x404': get_nested(json_data, base_path + ['thumbnail', 'thumbnails', 1, 'url']),
        'title_text': get_nested(json_data, base_path + ['title', 'runs', 0, 'text']),
        'title_label': get_nested(json_data, base_path + ['title', 'accessibility', 'accessibilityData', 'label']),
        'channel_url': get_nested(json_data, base_path + ['longBylineText', 'runs', 0, 'navigationEndpoint', 'commandMetadata', 'webCommandMetadata', 'url']),
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


videos_data = []
for i in range(10):
    video_data = extract_video_data(json_data, i)
    videos_data.append(video_data)  # Добавляем словарь с данными о видео в список

# Преобразуем список словарей в строку JSON с отступами в 4 пробела
json_str = json.dumps(videos_data, indent=4)

# Выводим строку JSON в консоль
print(json_str)


def json_write(data):
    with open('videos_data.json','w') as f:
        json.dump(data, f, indent=4)

