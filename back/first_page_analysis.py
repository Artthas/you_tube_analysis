import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/@chestniyblog/videos'

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru',
    'cache-control': 'max-age=0',
    # 'cookie': 'GPS=1; YSC=lKgeMWRqPYw; VISITOR_INFO1_LIVE=kh6IXtAFs8w; PREF=f4=4000000&tz=Europe.Belgrade',
    'dnt': '1',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"115.0.5790.98"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="99.0.0.0", "Google Chrome";v="115.0.5790.98", "Chromium";v="115.0.5790.98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '"5.19.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'

proxies = {
    'http': proxy_url,
    'https': proxy_url,
}

# response = requests.get('https://www.youtube.com/@chestniyblog/videos',headers=headers)


# with open('page.html', 'a') as f:
#     f.write(response.text)

with open('page.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'lxml')

scripts = soup.find_all('script')
for script in scripts:
    if 'ytInitialData' in script.text:
        json_str = script.text
        break

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
"""

# print(json_str)
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