import json

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from first_page_analysis import *
from parse_youtube_search import *
import traceback
import asyncio
import logging
from utils import find_new_titles
from chat_gpt_api import create_ideas
from parse_concurence import func_for_titles_competitors
app = FastAPI()

origins = [
    "http://185.213.211.3:3020",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)




MAX_RETRIES = 4  # Количество попыток

@app.get("/get_you_tube_by_channel/")
async def get_keys(channel_name: str):
    """
    Асинхронная функция для получения данных о видео на YouTube по имени канала.

    :param channel_name: Имя канала на YouTube, для которого необходимо получить данные.
    :return: JSON-объект с данными о видео или ошибкой, если что-то пошло не так.
    """

    # Логирование полученного имени канала
    logger.info(f"Received channel_name: {channel_name}")

    for _ in range(MAX_RETRIES):
        try:
            # Получение ключевых слов для поиска видео по имени канала
            info_from_gpt = await general_func(channel_name)
            dict_from_gpt = info_from_gpt[0]

            # он в формате словари с данными о видео где есть title, url, thumbnail и все они находятся в списке
            dict_to_front = info_from_gpt[1] # TODO вернуть на фронт для отображения на странице, типа из чего генрим идеи
            # print(dict_to_front)
            keys = dict_from_gpt["formatted_keywords"]
            old_titles = dict_from_gpt["first_titles"]
            description = dict_from_gpt['description']
            print('HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHaaaaaaaaaaaaaaaaaa')
            # print(description)
            general_channel = {channel_name: old_titles}
            # Логирование сгенерированных ключевых слов
            logger.info(f"Generated keys: {keys}")


            """
            здесь я получаю словарь где будет инфа о видео, о первых 20ти из поиска ютуба
            так же здесь я должен брать ссылки на каналы и парсить там видео
            """
            first_json = await general_YT(search_query=keys, quantity=20)
            # Если final_json пуст, то вызываем исключение, чтобы повторить попытку
            if not first_json:
                await asyncio.sleep(3)  # Задержка перед повторной попыткой

                raise ValueError("Received empty JSON response")

            # здесь я ищу новые заголовки для видео
            new_titles_raw = find_new_titles(video_list=first_json, channel_name=channel_name)
            # нахожу конкурентов
            competitors_links_not_will_use = new_titles_raw[1]
            competitors_raw = [url.split('@')[1] for url in new_titles_raw[1]]

            if len(competitors_raw) > 3:
                selected_competitors = competitors_raw[:3]  # берем первые 3
            elif 0 < len(competitors_raw) <= 3:
                selected_competitors = [competitors_raw[0]]  # берем только первый
            else:
                selected_competitors = []

            competitors = await func_for_titles_competitors(selected_competitors)
            # list_with_comptetitors_url_to_front = [f"https://www.youtube.com/@{name}/videos" for name in
            #                                        competitors.keys() if len(competitors) >= 1]
            list_with_comptetitors_url_to_front = []

            if len(competitors) > 1:
                for channel_dict in competitors:
                    for channel_name in channel_dict.keys():
                        list_with_comptetitors_url_to_front.append(f"https://www.youtube.com/@{channel_name}/videos")


            # try:
            #     print(json.dumps(competitors, indent=4))
            # except:
            #     print(competitors)
            # print(selected_competitors)
            # print(general_channel)
            # TODO вызываю анализ каналов конкурентов
            print('***************************************************')
            print(list_with_comptetitors_url_to_front) # TODO тоже на фронт. Типа с каких каналов идеи
            # print(keys)
            # print(old_titles)
            # print(new_titles)


            ideas = await create_ideas(general_ch=general_channel, comp_ch_list=competitors)
            print('***************************************************')
            print(json.dumps(ideas, indent=4))

            # Возврат данных в формате JSON
            return {"final_json": first_json}

        except HTTPException as e:
            error_message = str(e.detail) if hasattr(e, 'detail') else str(e)
            error_traceback = traceback.format_exc()
            full_error_message = f"{error_message}\n{error_traceback}"
            logger.error(f"Error occurred get_keys: {full_error_message}")
            if _ == MAX_RETRIES - 1:
                return {"error get_keys": full_error_message}
            await asyncio.sleep(3)

        except Exception as e:
            error_message = str(e) + "\n" + traceback.format_exc()
            logger.error(f"Error occurred get_keys: {error_message}")
            if _ == MAX_RETRIES - 1:
                return {"error": error_message}
            await asyncio.sleep(3)
