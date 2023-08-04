import requests

cookies = {
    'YSC': 'D81u9Jv05N8',
    'VISITOR_INFO1_LIVE': 'x7_ah2100lk',
    'DEVICE_INFO': 'ChxOekU1T0RVNE1ETTFNREUxTWpBMk16ZzJOZz09ELD9mZ8GGLD9mZ8G',
    'wide': '1',
    'PREF': 'tz=Europe.Belgrade&f4=4000000&f5=20000',
    'SID': 'ZAg9ik-RCwF3ZT1eGc9vu9fpvUsF84tNHdvNNMleO2n2LtplXGkWgD3lg14aH03xUE3dHg.',
    '__Secure-1PSID': 'ZAg9ik-RCwF3ZT1eGc9vu9fpvUsF84tNHdvNNMleO2n2LtplUYATH-nGb5NuBocwcXR5Iw.',
    '__Secure-3PSID': 'ZAg9ik-RCwF3ZT1eGc9vu9fpvUsF84tNHdvNNMleO2n2Ltpl54sBa89nBKH4fYOq8xVZhw.',
    'HSID': 'ADk-qaTVnykkLIYbi',
    'SSID': 'A9rQmdegx-rCw88Yw',
    'APISID': 'ayKLAL2ru1kdpaL5/APf5ScGI3_wjGNIMX',
    'SAPISID': 'TdTh6QuGnFg9zwhX/AFCWXG3Dd20JwkYtN',
    '__Secure-1PAPISID': 'TdTh6QuGnFg9zwhX/AFCWXG3Dd20JwkYtN',
    '__Secure-3PAPISID': 'TdTh6QuGnFg9zwhX/AFCWXG3Dd20JwkYtN',
    'LOGIN_INFO': 'AFmmF2swRQIhALZf4qpZqxS7eOSxxsahQFQGhKwjJsTcFGIDAPbeFpDjAiBm9TRHGWmUpffAa_-xX-bG7gfXRouWXfR0fOC1U3e34A:QUQ3MjNmeVBidU5FSUo3MHI5YnVPUW9sM2VNQThPcUlpR194UThhUm9KMXJXSHMtY2xPSEFmd1ZOSUxMMXo2QXdYSGltRk5nR3E0X2UzU1RPQnFQcElhQkMwZ2JSN0Z5VVFMUnhHcnZCT2JrNHBxazdKZ1lxWmYyQ2M1UDdHYk82bzZmX0RFTHQ5VVFQd3FJeUxCWmY1YmlPVml2NGJtWVlR',
    '__Secure-1PSIDTS': 'sidts-CjEBSAxbGeyUDfJzAY69aQQhl88ox5dn_bWkoe8yjIEstYcOVkpDJGqsSn0f6FNKXFJeEAA',
    '__Secure-3PSIDTS': 'sidts-CjEBSAxbGeyUDfJzAY69aQQhl88ox5dn_bWkoe8yjIEstYcOVkpDJGqsSn0f6FNKXFJeEAA',
    'ST-pon046': 'itct=CBkQk3UYAyITCKyIo7Cyw4ADFb7hEQgdX7APjA%3D%3D&csn=MC4yOTM1OTI5MDgxOTc5NjczNQ..&endpoint=%7B%22clickTrackingParams%22%3A%22CBkQk3UYAyITCKyIo7Cyw4ADFb7hEQgdX7APjA%3D%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fresults%3Fsearch_query%3D%25D0%2598%25D0%25BD%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%257C%2B%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2586%25D0%25B8%25D1%258F%2B%257C%2B%25D0%259A%25D0%2595%25D0%2593%25D0%25AD%2B%257C%2B%25D0%25A4%25D0%25BE%25D0%25BA%25D1%2581%25D1%2584%25D0%25BE%25D1%2580%25D0%25B4%2B%257C%2BPython%2B3%2B%257C%2B%25D0%2590%25D0%25BB%25D0%25B3%25D0%25BE%25D1%2580%25D0%25B8%25D1%2582%25D0%25BC%25D1%258B%2B%257C%2B%25D0%25BF%25D1%2580%25D0%25B0%25D0%25BA%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D1%258F%2B%257C%2B%25D0%25BA%25D0%25BE%25D0%25B4%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5%2B%257C%2B%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D1%258B%25D0%25B9%2B%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%26sp%3DCAESBAgFEAE%25253D%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_SEARCH%22%2C%22rootVe%22%3A4724%7D%7D%2C%22searchEndpoint%22%3A%7B%22query%22%3A%22%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%7C%20%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%20%7C%20%D0%9A%D0%95%D0%93%D0%AD%20%7C%20%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4%20%7C%20Python%203%20%7C%20%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20%7C%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%7C%20%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%7C%20%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%B3%D1%80%D0%B0%D1%84%22%2C%22params%22%3A%22CAESBAgFEAE%253D%22%7D%7D',
    'SIDCC': 'APoG2W8q4S_LulU4VSoar4fw1Luk6lCMaJ4G69xP_PQCyCGnYTc0HSygfDN6aKXY5BDcfsoNwg',
    '__Secure-1PSIDCC': 'APoG2W__1Uw_z4jwKYPUa3Xs1Tzxoq-LLfsm6PuHs3CKIj7Z8N94CCPPniM-YveGXoFVexXOBA',
    '__Secure-3PSIDCC': 'APoG2W8kbSE50nLO4LjeZ32JCTyMwRqeylhdrBbdfl8UreTqVfpOKnBziyMb-l92qNwk2bZXDg',
    'ST-tts1u6': 'itct=CBoQk3UYAiITCK6N57ayw4ADFXbHEQgdV-cNaQ%3D%3D&csn=MC40NzA2MjA4MzU4NzcyNDk3&endpoint=%7B%22clickTrackingParams%22%3A%22CBoQk3UYAiITCK6N57ayw4ADFXbHEQgdV-cNaQ%3D%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fresults%3Fsearch_query%3D%25D0%2598%25D0%25BD%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%257C%2B%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2586%25D0%25B8%25D1%258F%2B%257C%2B%25D0%259A%25D0%2595%25D0%2593%25D0%25AD%2B%257C%2B%25D0%25A4%25D0%25BE%25D0%25BA%25D1%2581%25D1%2584%25D0%25BE%25D1%2580%25D0%25B4%2B%257C%2BPython%2B3%2B%257C%2B%25D0%2590%25D0%25BB%25D0%25B3%25D0%25BE%25D1%2580%25D0%25B8%25D1%2582%25D0%25BC%25D1%258B%2B%257C%2B%25D0%25BF%25D1%2580%25D0%25B0%25D0%25BA%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D1%258F%2B%257C%2B%25D0%25BA%25D0%25BE%25D0%25B4%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5%2B%257C%2B%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D1%258B%25D0%25B9%2B%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%26sp%3DCAMSBAgFEAE%25253D%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_SEARCH%22%2C%22rootVe%22%3A4724%7D%7D%2C%22searchEndpoint%22%3A%7B%22query%22%3A%22%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%7C%20%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%20%7C%20%D0%9A%D0%95%D0%93%D0%AD%20%7C%20%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4%20%7C%20Python%203%20%7C%20%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20%7C%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%7C%20%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%7C%20%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%B3%D1%80%D0%B0%D1%84%22%2C%22params%22%3A%22CAMSBAgFEAE%253D%22%7D%7D',
}

headers = {
    'authority': 'www.youtube.com',
    'accept': '*/*',
    'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
    'authorization': 'SAPISIDHASH 1691165502_6fd4c9e863d99999e666be985b083b27ae5f9ba9',
    'content-type': 'application/json',
    # 'cookie': 'YSC=D81u9Jv05N8; VISITOR_INFO1_LIVE=x7_ah2100lk; DEVICE_INFO=ChxOekU1T0RVNE1ETTFNREUxTWpBMk16ZzJOZz09ELD9mZ8GGLD9mZ8G; wide=1; PREF=tz=Europe.Belgrade&f4=4000000&f5=20000; SID=ZAg9ik-RCwF3ZT1eGc9vu9fpvUsF84tNHdvNNMleO2n2LtplXGkWgD3lg14aH03xUE3dHg.; __Secure-1PSID=ZAg9ik-RCwF3ZT1eGc9vu9fpvUsF84tNHdvNNMleO2n2LtplUYATH-nGb5NuBocwcXR5Iw.; __Secure-3PSID=ZAg9ik-RCwF3ZT1eGc9vu9fpvUsF84tNHdvNNMleO2n2Ltpl54sBa89nBKH4fYOq8xVZhw.; HSID=ADk-qaTVnykkLIYbi; SSID=A9rQmdegx-rCw88Yw; APISID=ayKLAL2ru1kdpaL5/APf5ScGI3_wjGNIMX; SAPISID=TdTh6QuGnFg9zwhX/AFCWXG3Dd20JwkYtN; __Secure-1PAPISID=TdTh6QuGnFg9zwhX/AFCWXG3Dd20JwkYtN; __Secure-3PAPISID=TdTh6QuGnFg9zwhX/AFCWXG3Dd20JwkYtN; LOGIN_INFO=AFmmF2swRQIhALZf4qpZqxS7eOSxxsahQFQGhKwjJsTcFGIDAPbeFpDjAiBm9TRHGWmUpffAa_-xX-bG7gfXRouWXfR0fOC1U3e34A:QUQ3MjNmeVBidU5FSUo3MHI5YnVPUW9sM2VNQThPcUlpR194UThhUm9KMXJXSHMtY2xPSEFmd1ZOSUxMMXo2QXdYSGltRk5nR3E0X2UzU1RPQnFQcElhQkMwZ2JSN0Z5VVFMUnhHcnZCT2JrNHBxazdKZ1lxWmYyQ2M1UDdHYk82bzZmX0RFTHQ5VVFQd3FJeUxCWmY1YmlPVml2NGJtWVlR; __Secure-1PSIDTS=sidts-CjEBSAxbGeyUDfJzAY69aQQhl88ox5dn_bWkoe8yjIEstYcOVkpDJGqsSn0f6FNKXFJeEAA; __Secure-3PSIDTS=sidts-CjEBSAxbGeyUDfJzAY69aQQhl88ox5dn_bWkoe8yjIEstYcOVkpDJGqsSn0f6FNKXFJeEAA; ST-pon046=itct=CBkQk3UYAyITCKyIo7Cyw4ADFb7hEQgdX7APjA%3D%3D&csn=MC4yOTM1OTI5MDgxOTc5NjczNQ..&endpoint=%7B%22clickTrackingParams%22%3A%22CBkQk3UYAyITCKyIo7Cyw4ADFb7hEQgdX7APjA%3D%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fresults%3Fsearch_query%3D%25D0%2598%25D0%25BD%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%257C%2B%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2586%25D0%25B8%25D1%258F%2B%257C%2B%25D0%259A%25D0%2595%25D0%2593%25D0%25AD%2B%257C%2B%25D0%25A4%25D0%25BE%25D0%25BA%25D1%2581%25D1%2584%25D0%25BE%25D1%2580%25D0%25B4%2B%257C%2BPython%2B3%2B%257C%2B%25D0%2590%25D0%25BB%25D0%25B3%25D0%25BE%25D1%2580%25D0%25B8%25D1%2582%25D0%25BC%25D1%258B%2B%257C%2B%25D0%25BF%25D1%2580%25D0%25B0%25D0%25BA%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D1%258F%2B%257C%2B%25D0%25BA%25D0%25BE%25D0%25B4%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5%2B%257C%2B%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D1%258B%25D0%25B9%2B%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%26sp%3DCAESBAgFEAE%25253D%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_SEARCH%22%2C%22rootVe%22%3A4724%7D%7D%2C%22searchEndpoint%22%3A%7B%22query%22%3A%22%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%7C%20%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%20%7C%20%D0%9A%D0%95%D0%93%D0%AD%20%7C%20%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4%20%7C%20Python%203%20%7C%20%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20%7C%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%7C%20%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%7C%20%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%B3%D1%80%D0%B0%D1%84%22%2C%22params%22%3A%22CAESBAgFEAE%253D%22%7D%7D; SIDCC=APoG2W8q4S_LulU4VSoar4fw1Luk6lCMaJ4G69xP_PQCyCGnYTc0HSygfDN6aKXY5BDcfsoNwg; __Secure-1PSIDCC=APoG2W__1Uw_z4jwKYPUa3Xs1Tzxoq-LLfsm6PuHs3CKIj7Z8N94CCPPniM-YveGXoFVexXOBA; __Secure-3PSIDCC=APoG2W8kbSE50nLO4LjeZ32JCTyMwRqeylhdrBbdfl8UreTqVfpOKnBziyMb-l92qNwk2bZXDg; ST-tts1u6=itct=CBoQk3UYAiITCK6N57ayw4ADFXbHEQgdV-cNaQ%3D%3D&csn=MC40NzA2MjA4MzU4NzcyNDk3&endpoint=%7B%22clickTrackingParams%22%3A%22CBoQk3UYAiITCK6N57ayw4ADFXbHEQgdV-cNaQ%3D%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fresults%3Fsearch_query%3D%25D0%2598%25D0%25BD%25D1%2584%25D0%25BE%25D1%2580%25D0%25BC%25D0%25B0%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%257C%2B%25D0%25BB%25D0%25B5%25D0%25BA%25D1%2586%25D0%25B8%25D1%258F%2B%257C%2B%25D0%259A%25D0%2595%25D0%2593%25D0%25AD%2B%257C%2B%25D0%25A4%25D0%25BE%25D0%25BA%25D1%2581%25D1%2584%25D0%25BE%25D1%2580%25D0%25B4%2B%257C%2BPython%2B3%2B%257C%2B%25D0%2590%25D0%25BB%25D0%25B3%25D0%25BE%25D1%2580%25D0%25B8%25D1%2582%25D0%25BC%25D1%258B%2B%257C%2B%25D0%25BF%25D1%2580%25D0%25B0%25D0%25BA%25D1%2582%25D0%25B8%25D0%25BA%25D0%25B0%2B%25D0%25BF%25D1%2580%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D0%25BC%25D0%25BC%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D1%258F%2B%257C%2B%25D0%25BA%25D0%25BE%25D0%25B4%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5%2B%257C%2B%25D0%25BE%25D1%2580%25D0%25B8%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B8%25D1%2580%25D0%25BE%25D0%25B2%25D0%25B0%25D0%25BD%25D0%25BD%25D1%258B%25D0%25B9%2B%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%26sp%3DCAMSBAgFEAE%25253D%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_SEARCH%22%2C%22rootVe%22%3A4724%7D%7D%2C%22searchEndpoint%22%3A%7B%22query%22%3A%22%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%7C%20%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%20%7C%20%D0%9A%D0%95%D0%93%D0%AD%20%7C%20%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4%20%7C%20Python%203%20%7C%20%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20%7C%20%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%7C%20%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%20%7C%20%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%B3%D1%80%D0%B0%D1%84%22%2C%22params%22%3A%22CAMSBAgFEAE%253D%22%7D%7D',
    'dnt': '1',
    'origin': 'https://www.youtube.com',
    'referer': 'https://www.youtube.com/results?search_query=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0+%7C+%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F+%7C+%D0%9A%D0%95%D0%93%D0%AD+%7C+%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4+%7C+Python+3+%7C+%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B+%7C+%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%7C+%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%7C+%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9+%D0%B3%D1%80%D0%B0%D1%84&sp=CAMSBAgFEAE%253D',
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
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'same-origin',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-client-data': 'CJS2yQEIo7bJAQipncoBCN7iygEIkqHLAQj8qswBCIWTzQEIh6DNAQj1sc0BCNq0zQEIsr3NAQjcvc0BCLy+zQEI38TNAQjvxM0BCKrFzQEI9cXNAQi3yM0BCLvIzQEYjKfNAQ==',
    'x-goog-authuser': '0',
    'x-goog-visitor-id': 'Cgt4N19haDIxMDBsayioxrSmBg%3D%3D',
    'x-origin': 'https://www.youtube.com',
    'x-youtube-bootstrap-logged-in': 'true',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20230803.01.00',
}

params = {
    'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    'prettyPrint': 'false',
}

json_data = {
    'context': {
        'client': {
            'hl': 'ru',
            'gl': 'ME',
            'remoteHost': '62.4.55.245',
            'deviceMake': '',
            'deviceModel': '',
            'visitorData': 'Cgt4N19haDIxMDBsayioxrSmBg%3D%3D',
            'userAgent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20230803.01.00',
            'osName': 'X11',
            'osVersion': '',
            'originalUrl': 'https://www.youtube.com/results?search_query=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0+%7C+%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F+%7C+%D0%9A%D0%95%D0%93%D0%AD+%7C+%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4+%7C+Python+3+%7C+%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B+%7C+%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%7C+%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%7C+%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9+%D0%B3%D1%80%D0%B0%D1%84&sp=CAMSBAgFEAE%253D',
            'screenPixelDensity': 1,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': 'CKjGtKYGEInorgUQls6vBRDqw68FEKy3rwUQk9n-EhCCpa8FEIXZ_hIQqcSvBRDUoa8FEJLLrwUQ-r6vBRCSz68FELWmrwUQmtGvBRDetq8FEOe6rwUQpN6vBRD956gYENuvrwUQuIuuBRCPo68FEOC2rwUQlM-vBRCMy68FEMzfrgUQpcL-EhDcz68FEOLUrgUQndv-EhCMt68FEPOorwUQtMmvBRDB3v4SEOuTrgUQ7qKvBRDks_4SEL22rgUQzK7-EhCPw68FEJfPrwU%3D',
            },
            'screenDensityFloat': 1.25,
            'timeZone': 'Europe/Belgrade',
            'browserName': 'Chrome',
            'browserVersion': '115.0.0.0',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'deviceExperimentId': 'ChxOekU1T0RVNE1ETTFNREUxTWpBMk16ZzJOZz09EKjGtKYGGLD9mZ8G',
            'screenWidthPoints': 942,
            'screenHeightPoints': 699,
            'utcOffsetMinutes': 120,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
            'memoryTotalKbytes': '8000000',
            'mainAppWebInfo': {
                'graftUrl': '/results?search_query=%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0+%7C+%D0%BB%D0%B5%D0%BA%D1%86%D0%B8%D1%8F+%7C+%D0%9A%D0%95%D0%93%D0%AD+%7C+%D0%A4%D0%BE%D0%BA%D1%81%D1%84%D0%BE%D1%80%D0%B4+%7C+Python+3+%7C+%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B+%7C+%D0%BF%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D0%BA%D0%B0+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F+%7C+%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5+%7C+%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9+%D0%B3%D1%80%D0%B0%D1%84&sp=CAMSBAgFEAE%253D',
                'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_UNKNOWN',
                'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                'isWebNativeShareAvailable': False,
            },
        },
        'user': {
            'lockedSafetyMode': False,
        },
        'request': {
            'useSsl': True,
            'internalExperimentFlags': [],
            'consistencyTokenJars': [],
        },
        'clickTracking': {
            'clickTrackingParams': 'CBoQk3UYAiITCK6N57ayw4ADFXbHEQgdV-cNaQ==',
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': '1691165480331',
                },
                {
                    'key': 'flash',
                    'value': '0',
                },
                {
                    'key': 'frm',
                    'value': '0',
                },
                {
                    'key': 'u_tz',
                    'value': '120',
                },
                {
                    'key': 'u_his',
                    'value': '3',
                },
                {
                    'key': 'u_h',
                    'value': '864',
                },
                {
                    'key': 'u_w',
                    'value': '1536',
                },
                {
                    'key': 'u_ah',
                    'value': '837',
                },
                {
                    'key': 'u_aw',
                    'value': '1536',
                },
                {
                    'key': 'u_cd',
                    'value': '24',
                },
                {
                    'key': 'bc',
                    'value': '31',
                },
                {
                    'key': 'bih',
                    'value': '699',
                },
                {
                    'key': 'biw',
                    'value': '927',
                },
                {
                    'key': 'brdim',
                    'value': '0,56,0,56,1536,27,1536,808,942,699',
                },
                {
                    'key': 'vis',
                    'value': '1',
                },
                {
                    'key': 'wgl',
                    'value': 'true',
                },
                {
                    'key': 'ca_type',
                    'value': 'image',
                },
            ],
            'bid': 'ANyPxKpHBPddwPH6h9t4tH-vVAq_hWayYOT6-tYrX2ZaTiIIm5ta6pSmf65pyH4MuN5a-2duUh_b',
        },
    },
    'query': 'Информатика | лекция | КЕГЭ | Фоксфорд | Python 3 | Алгоритмы | практика программирования | кодирование | ориентированный граф',
    'params': 'CAMSBAgFEAE%3D',
}

response = requests.post(
    'https://www.youtube.com/youtubei/v1/search',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

print(response)