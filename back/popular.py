import json
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.youtube.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru',
    'cache-control': 'max-age=0',
    # 'cookie': 'GPS=1; YSC=KeL97jZDIMU; VISITOR_INFO1_LIVE=cvOPlVmgc8A; PREF=f4=4000000&tz=Europe.Belgrade',
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
    'sec-fetch-site': 'none',
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

url2 = 'https://www.youtube.com/@chestniyblog/videos'
response = requests.get(url2, headers=headers, proxies=proxies)

soup = BeautifulSoup(response.text, 'lxml')
scripts = soup.find_all('script')
for script in scripts:
    if 'ytInitialData' in script.text:
        json_str = script.text
        break


json_str = json_str.split('var ytInitialData =')[1]
json_str = json_str.rsplit('};', 1)[0] + '}'
data = json.loads(json_str)
# print(json.dumps(data, indent=4))
with open('my_jsonNEW.json', 'a', encoding='utf-8') as j1:
    j1.write(json.dumps(data, indent=4, ensure_ascii=False))