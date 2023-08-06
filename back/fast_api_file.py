# from first_page_analysis import *
# from parse_youtube_search import *
#
# channel_name1 = 'chestniyblog'
# channel_name2 = 'nickiminaj'
# channel_name3 = 'DontTellComedy'
# channel_name4 = 'python228dlapypsikov'
# channel_name5 = 'tkhirianov'
#
# keys = general_func(channel_name3)
# final_json = general_YT(search_query=keys, quantity=10)
# print(final_json)
# uvicorn fast_api_file:app --reload

from fastapi import FastAPI, HTTPException, Query
from first_page_analysis import *
from parse_youtube_search import *

import logging

app = FastAPI()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/get_you_tube_by_channel/")
async def get_keys(channel_name: str):
    logger.info(f"Received channel_name: {channel_name}")
    try:
        keys = await general_func(channel_name)
        logger.info(f"Generated keys: {keys}")
        final_json = await general_YT(search_query=keys, quantity=10)
        print(final_json)
        return {"final_json": final_json}
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}


