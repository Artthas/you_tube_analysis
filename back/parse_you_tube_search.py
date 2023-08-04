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
    'search_query': """Stand-Up Comedy | stand up comedy | stand up | comedians stand up comedy | standup comedy | stand-up comedy | dont tell comedy | don't tell comedy | mark smalls | michael longfellow | secret comedy shows | backyard comedy shows | funny jokes | comedy specials | best comedians""",
    # 'search_query': 'какой телефон лучше | тест камер | dj feel | опыт использования | русский russian | честный блог | redmi note 8 pro | iphone 11 pro | iphone se | купить смартфон | какой смартфон купить | честный блог | s22 ultra | poco x3 pro | iphone 14 pro | xiaomi 12s ultra | pixel 7 pro | pixel 6 pro | самсунг с22 | пиксель 7 про',
    # 'search_query': 'Nicki Minaj | young money | cash money | republic records | lil wayne | Pink Friday | Super Bass | Anaconda Nicki | city girls | kash doll | megan thee stallion',
    # 'search_query': 'Информатика | лекция | КЕГЭ | Фоксфорд | Python 3 | Алгоритмы | практика программирования | кодирование | ориентированный граф',
    'sp': 'CAMSAggF',
    # 'sp': 'CAESBAgFEAE%3D',
    # 'sp': 'CAMSBAgFEAE%3D'
}

# response = requests.get('https://www.youtube.com/results', params=params, headers=headers)
# print(response.url)

# with open('result11.html', 'a') as f:
#     f.write(response.text)
# print(response.text)

with open('result11.html', 'r') as f:
    content = f.read()

soup = BeautifulSoup(content, 'lxml')
scripts = soup.find_all('script')

for script in scripts:
    if 'ytInitialData' in script.text:
        json_str = script.text
        break
json_str = json_str.split('var ytInitialData =')[1]
json_str = json_str.rsplit('};', 1)[0] + '}'
data = json.loads(json_str)

# with open('res.json', 'a') as f:
#     json.dump(data, f, indent=4)
