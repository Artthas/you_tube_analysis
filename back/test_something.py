import asyncio
import json
from dotenv import load_dotenv
import requests
load_dotenv()

TOKEN = load_dotenv('API_TOKEN_scrapestorm')

# q = f'https://scrapestorm.net/youtube.com/api/v2.1/get_channel_videos?token={TOKEN}&query=thefugitiveofficial'
# q2 = f'https://scrapestorm.net/youtube.com/api/v1.1/get_channel_videos?token={TOKEN}&query=thefugitiveofficial'
# resp = requests.get(q2)

# with open('leshajson.json', 'a') as f:
#     f.write(json.dumps(resp.json(), indent=4))
# print(json.dumps(resp.json(), indent=4))
# print(resp.json())


"""
from fastapi import HTTPException

@app.get("/scrape/{channel_name}")
async def scrape_channel(channel_name: str):
    yt_scrap = YouTubeScraper()
    await yt_scrap.create_session()
    try:
        await yt_scrap.get_first_page_data(channel_name)
        d = yt_scrap.data_with_new_video
        return d
    except HTTPException as e:
        raise e
    finally:
        await yt_scrap.close_session()
        
        """




