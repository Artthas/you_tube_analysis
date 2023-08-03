import requests
import json




def find_popular_video_titles(channel_name, token):
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

    response = requests.post(
        'https://www.youtube.com/youtubei/v1/browse',
        headers=headers,
        json=json_data,
    )

    video_titles = []
    try:
        items = response.json()['onResponseReceivedActions'][1]['reloadContinuationItemsCommand']['continuationItems']
        for item in items[:5]:
            title = item['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
            video_titles.append(title)
    except Exception as e:
        print(f"An error occurred: {e}")

    return video_titles

# channel_name = 'nickiminaj'
# token = 'YOUR_TOKEN_HERE'
# titles = find_popular_video_titles(channel_name, token)
# print(titles)
