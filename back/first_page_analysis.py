# import requests
# from bs4 import BeautifulSoup
#
#
# url = 'https://www.youtube.com/@chestniyblog/videos'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
#     'X-YouTube-Client-Name': '1',
#     'X-YouTube-Client-Version': '2.20230725.01.00',
# }
#
# token_page = requests.get(url, headers=headers)
# with open('page.html', 'a') as f:
#     f.write(token_page.text)

import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/@chestniyblog/videos'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'X-YouTube-Client-Name': '1',
    'X-YouTube-Client-Version': '2.20230725.01.00',
}

proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'

proxies = {
    'http': proxy_url,
    'https': proxy_url,
}

# token_page = requests.get(url, headers=headers, proxies=proxies)
# with open('pag2e.html', 'a', encoding='utf-8') as f:
#     f.write(token_page.text)

with open('pag2e.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'lxml')


print(soup)