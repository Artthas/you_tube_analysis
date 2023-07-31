import json
import requests
from bs4 import BeautifulSoup

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

def find_continuation_tokens(data):
    """Функция для извлечения токенов продолжения из данных JSON."""
    path_to_continuation = ["continuationCommand", "token"]
    for key, value in data.items():
        if key == "continuationCommand":
            yield get_value_by_path(value, path_to_continuation)
        elif isinstance(value, dict):
            yield from find_continuation_tokens(value)
        elif isinstance(value, list):
            for item in value:
                yield from find_continuation_tokens(item)

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
                print(f"Title {i+1}: {title}")
            if len(titles) >= max_titles:
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    return titles


def get_channel_data(channel_url):
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
    response = requests.get(url=channel_url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(response.text, 'lxml')
    scripts = soup.find_all('script')
    for script in scripts:
        if 'ytInitialData' in script.text:
            json_str = script.text
            break

    json_str = json_str.split('var ytInitialData =')[1]
    json_str = json_str.rsplit('};', 1)[0] + '}'
    data = json.loads(json_str)

    return data


def main():
    channel_url = "https://www.youtube.com/@chestniyblog/videos"
    data = get_channel_data(channel_url)
    tokens = list(find_continuation_tokens(data))
    print("Continuation tokens:", tokens)
    titles = find_video_titles(data)
    print("Video titles:", titles)

if __name__ == "__main__":
    main()

