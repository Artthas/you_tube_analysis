import requests


url = 'https://www.youtube.com/@chestniyblog/videos'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'X-YouTube-Client-Name': '1',
    'X-YouTube-Client-Version': '2.20230725.01.00',
}

token_page = requests.get(url, headers=headers)
