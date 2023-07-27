import requests

cookies = {
    'GPS': '1',
    'YSC': 'KeL97jZDIMU',
    'VISITOR_INFO1_LIVE': 'cvOPlVmgc8A',
    'PREF': 'f4=4000000&tz=Europe.Belgrade',
}

headers = {
    'authority': 'www.youtube.com',
    'accept': '*/*',
    'accept-language': 'ru',
    'content-type': 'application/json',
    # 'cookie': 'GPS=1; YSC=KeL97jZDIMU; VISITOR_INFO1_LIVE=cvOPlVmgc8A; PREF=f4=4000000&tz=Europe.Belgrade',
    'dnt': '1',
    'origin': 'https://www.youtube.com',
    'referer': 'https://www.youtube.com/@chestniyblog/videos',
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
    'x-goog-visitor-id': 'Cgtjdk9QbFZtZ2M4QSjA7oqmBg%3D%3D',
    'x-youtube-bootstrap-logged-in': 'false',
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20230725.07.00',
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
            'remoteHost': '62.4.55.242',
            'deviceMake': '',
            'deviceModel': '',
            'visitorData': 'Cgtjdk9QbFZtZ2M4QSjA7oqmBg%3D%3D',
            'userAgent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36,gzip(gfe)',
            'clientName': 'WEB',
            'clientVersion': '2.20230725.07.00',
            'osName': 'X11',
            'osVersion': '',
            'originalUrl': 'https://www.youtube.com/@chestniyblog/videos',
            'screenPixelDensity': 1,
            'platform': 'DESKTOP',
            'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
            'configInfo': {
                'appInstallData': 'CMDuiqYGEOLUrgUQtMmvBRDcz68FEJrRrwUQ_eeoGBCSy68FEMy3_hIQ57qvBRCx1a8FEOSz_hIQqrL-EhCEtq8FENuvrwUQzN-uBRCF2f4SEPq-rwUQieiuBRCpxK8FEIy3rwUQtuCuBRCQo68FEJbOrwUQ6sOvBRDUoa8FEKy3rwUQgqWvBRC4i64FEL22rgUQ3ravBRDjzv4SEMO3_hIQndv-EhDB3v4SEOuTrgUQ3cavBRD-ta8FEI_DrwUQuNWvBRD4ta8FELWmrwUQpcL-EhCMy68FEPOorwUQzK7-EhDuoq8FEOC2rwUQtLKvBRDyvq8FEPvWrwU%3D',
            },
            'screenDensityFloat': 1.25,
            'timeZone': 'Europe/Belgrade',
            'browserName': 'Chrome',
            'browserVersion': '115.0.0.0',
            'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'deviceExperimentId': 'ChxOekkyTURVMk56QXpOamMzT0Rnd05ERTVNdz09EMDuiqYGGMDuiqYG',
            'screenWidthPoints': 942,
            'screenHeightPoints': 726,
            'utcOffsetMinutes': 120,
            'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
            'connectionType': 'CONN_CELLULAR_4G',
            'memoryTotalKbytes': '8000000',
            'mainAppWebInfo': {
                'graftUrl': 'https://www.youtube.com/@chestniyblog/videos',
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
            'clickTrackingParams': 'CLkBEP1dGAEiEwiF7ZquxK-AAxW25REIHZ3qDSw=',
        },
        'adSignalsInfo': {
            'params': [
                {
                    'key': 'dt',
                    'value': '1690482497019',
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
                    'value': '11',
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
                    'value': '864',
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
                    'value': '726',
                },
                {
                    'key': 'biw',
                    'value': '927',
                },
                {
                    'key': 'brdim',
                    'value': '1536,29,1536,29,1536,0,1536,835,942,726',
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
        },
    },
    'continuation': '4qmFsgJkEhhVQ2MzaVJrTEQ1S0hLZktrNDAtZnNQMXcaSDhnWXVHaXg2S2hJbUNpUTJOR05oWm1FeE5DMHdNREF3TFRJME9EZ3RZamN4Wmkxa05HWTFORGRtT1RSbVl6Z1lBZyUzRCUzRA%3D%3D',
}

proxy_url = 'http://VxQpcz:4cb5aA@196.16.108.161:8000'

proxies = {
    'http': proxy_url,
    'https': proxy_url,
}
response = requests.post(
    'https://www.youtube.com/youtubei/v1/browse',

    headers=headers,
    json=json_data,
    proxies=proxies
)

print(response.text)
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"context":{"client":{"hl":"ru","gl":"ME","remoteHost":"62.4.55.242","deviceMake":"","deviceModel":"","visitorData":"Cgtjdk9QbFZtZ2M4QSjA7oqmBg%3D%3D","userAgent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20230725.07.00","osName":"X11","osVersion":"","originalUrl":"https://www.youtube.com/@chestniyblog/videos","screenPixelDensity":1,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CMDuiqYGEOLUrgUQtMmvBRDcz68FEJrRrwUQ_eeoGBCSy68FEMy3_hIQ57qvBRCx1a8FEOSz_hIQqrL-EhCEtq8FENuvrwUQzN-uBRCF2f4SEPq-rwUQieiuBRCpxK8FEIy3rwUQtuCuBRCQo68FEJbOrwUQ6sOvBRDUoa8FEKy3rwUQgqWvBRC4i64FEL22rgUQ3ravBRDjzv4SEMO3_hIQndv-EhDB3v4SEOuTrgUQ3cavBRD-ta8FEI_DrwUQuNWvBRD4ta8FELWmrwUQpcL-EhCMy68FEPOorwUQzK7-EhDuoq8FEOC2rwUQtLKvBRDyvq8FEPvWrwU%3D"},"screenDensityFloat":1.25,"timeZone":"Europe/Belgrade","browserName":"Chrome","browserVersion":"115.0.0.0","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOekkyTURVMk56QXpOamMzT0Rnd05ERTVNdz09EMDuiqYGGMDuiqYG","screenWidthPoints":942,"screenHeightPoints":726,"utcOffsetMinutes":120,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","connectionType":"CONN_CELLULAR_4G","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"https://www.youtube.com/@chestniyblog/videos","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_UNKNOWN","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":false}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"CLkBEP1dGAEiEwiF7ZquxK-AAxW25REIHZ3qDSw="},"adSignalsInfo":{"params":[{"key":"dt","value":"1690482497019"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"120"},{"key":"u_his","value":"11"},{"key":"u_h","value":"864"},{"key":"u_w","value":"1536"},{"key":"u_ah","value":"864"},{"key":"u_aw","value":"1536"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"726"},{"key":"biw","value":"927"},{"key":"brdim","value":"1536,29,1536,29,1536,0,1536,835,942,726"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"continuation":"4qmFsgJkEhhVQ2MzaVJrTEQ1S0hLZktrNDAtZnNQMXcaSDhnWXVHaXg2S2hJbUNpUTJOR05oWm1FeE5DMHdNREF3TFRJME9EZ3RZamN4Wmkxa05HWTFORGRtT1RSbVl6Z1lBZyUzRCUzRA%3D%3D"}'
#response = requests.post('https://www.youtube.com/youtubei/v1/browse', params=params, cookies=cookies, headers=headers, data=data)