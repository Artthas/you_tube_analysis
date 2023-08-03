import requests
import json

channel_name = 'nickiminaj'

"""
не понял
4qmFsgKCARIYVUMzak9kN0dVTWhwZ0pSQmhpTHp1THNnGmY4Z1pIR2tWNlF3b19DaGREWnpCTFF6QldibGRzVWxkU1NFSkZWVmR3VWtWQlFSSWtOalJrTTJFMVlUVXRNREF3TUMweU56RXpMV0pqWXpndE1qUXdOVGc0TnpGbVl6TmpHQUUlM0Q%3D
новые
4qmFsgJkEhhVQzNqT2Q3R1VNaHBnSlJCaGlMenVMc2caSDhnWXVHaXg2S2hJbUNpUTJOR1F6WVRWaE5TMHdNREF3TFRJM01UTXRZbU5qT0MweU5EQTFPRGczTVdaak0yTVlBUSUzRCUzRA%3D%3D
популярные
4qmFsgJkEhhVQzNqT2Q3R1VNaHBnSlJCaGlMenVMc2caSDhnWXVHaXg2S2hJbUNpUTJOR1F6WVRWaE5TMHdNREF3TFRJM01UTXRZbU5qT0MweU5EQTFPRGczTVdaak0yTVlBZyUzRCUzRA%3D%3D

4qmFsgJkEhhVQzNqT2Q3R1VNaHBnSlJCaGlMenVMc2caSDhnWXVHaXg2S2hJbUNpUTJOR1F6WVRWaE5TMHdNREF3TFRJM01UTXRZbU5qT0MweU5EQTFPRGczTVdaak0yTVlCQSUzRCUzRA%3D%3D
"""

"""
/onResponseReceivedActions/1/reloadContinuationItemsCommand/continuationItems/0/richItemRenderer/content/videoRenderer/title/runs/0/text

/onResponseReceivedActions/1/reloadContinuationItemsCommand/continuationItems/1/richItemRenderer/content/videoRenderer/title/runs/0/text
"""


def find_popular_video(channel_name, token):
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
                'configInfo': {
                    'appInstallData': 'CK32iqYGEKqy_hIQ5LP-EhCSy68FEOC2rwUQrLevBRDMt_4SEKXC_hIQ_rWvBRD4ta8FEJrRrwUQhLavBRCJ6K4FELiLrgUQndv-EhDqw68FENuvrwUQ28-vBRDnuq8FEMHe_hIQ86ivBRC41a8FEMO3_hIQhdn-EhCx1a8FELbgrgUQ65OuBRDi1K4FEKnErwUQtaavBRCWzq8FEPq-rwUQvbauBRCMt68FEI_DrwUQ3cavBRDUoa8FEP3nqBgQ7qKvBRDetq8FEMyu_hIQtMmvBRCMy68FEJCjrwUQgqWvBRDjzv4SEMzfrgUQtLKvBRD71q8FEPK-rwU%3D',
                },
                'screenDensityFloat': 1.25,
                'timeZone': 'Europe/Belgrade',
                'browserName': 'Chrome',
                'browserVersion': '115.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOekkyTURVM01UTTFNamsxTVRjNE1URTBOUT09EK32iqYGGK32iqYG',
                'screenWidthPoints': 942,
                'screenHeightPoints': 726,
                'utcOffsetMinutes': 120,
                'userInterfaceTheme': 'USER_INTERFACE_THEME_LIGHT',
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '8000000',
                'mainAppWebInfo': {
                    'graftUrl': f'https://www.youtube.com/@{channel_name}/videos',
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
                'clickTrackingParams': 'CLoBEP1dGAAiEwicvZnqxa-AAxVn1REIHc3JBiI=',
            },
        },
        'continuation': f'{token}',
    }

    response = requests.post(
        'https://www.youtube.com/youtubei/v1/browse',
        headers=headers,
        json=json_data,
    )

    # Save the response to a file
    with open('popular.json', 'w') as f:
        json.dump(response.json(), f, indent=4, sort_keys=True)
    print(response.json())

find_popular_video(channel_name='channel_name', token='4qmFsgJkEhhVQzNqT2Q3R1VNaHBnSlJCaGlMenVMc2caSDhnWXVHaXg2S2hJbUNpUTJOR1F6WVRWaE5TMHdNREF3TFRJM01UTXRZbU5qT0MweU5EQTFPRGczTVdaak0yTVlBZyUzRCUzRA')


"""
/onResponseReceivedActions/1/reloadContinuationItemsCommand/continuationItems/0/richItemRenderer/content/videoRenderer/title/runs/0/text"""