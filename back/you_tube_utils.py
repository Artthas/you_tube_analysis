from bs4 import BeautifulSoup
import json

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



def views_to_int(view_string):
    """
    Преобразует строку просмотров в число.

    :param view_string: Строка вида "4,599 views" или "11 million views".
    :return: Целое число просмотров.
    """
    # Если в строке есть слово "million", то умножаем число на 1,000,000
    if 'million' in view_string:
        number_part = float(''.join(c if c.isdigit() or c == '.' else '' for c in view_string))
        return int(number_part * 1_000_000)

    # Если в строке есть слово "billion", то умножаем число на 1,000,000,000
    elif 'billion' in view_string:
        number_part = float(''.join(c if c.isdigit() or c == '.' else '' for c in view_string))
        return int(number_part * 1_000_000_000)

    # Если в строке есть слово "thousand", то умножаем число на 1,000
    elif 'thousand' in view_string:
        number_part = int(''.join(filter(str.isdigit, view_string)))
        return number_part * 1_000

    # В противном случае просто возвращаем число
    else:
        return int(''.join(filter(str.isdigit, view_string)))



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

def make_json(json_data, quantity):
    videos_data = []
    for i in range(quantity):
        video_data = extract_video_data(json_data, i)
        # Если хотя бы одно значения в словаре равны None, пропускаем его
        if not any(value is None for value in video_data.values()):
            videos_data.append(video_data)  # Добавляем словарь с данными о видео в список

    return videos_data