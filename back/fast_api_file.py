from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from first_page_analysis import *
from parse_youtube_search import *

import logging

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


@app.get("/get_you_tube_by_channel/")
async def get_keys(channel_name: str):
    """
    Асинхронная функция для получения данных о видео на YouTube по имени канала.

    :param channel_name: Имя канала на YouTube, для которого необходимо получить данные.
    :return: JSON-объект с данными о видео или ошибкой, если что-то пошло не так.
    """

    # Логирование полученного имени канала
    logger.info(f"Received channel_name: {channel_name}")

    try:
        # Получение ключевых слов для поиска видео по имени канала
        keys = await general_func(channel_name)

        # Логирование сгенерированных ключевых слов
        logger.info(f"Generated keys: {keys}")

        # Получение данных о видео на YouTube с использованием ключевых слов
        final_json = await general_YT(search_query=keys, quantity=10)

        # Вывод полученных данных в консоль (можно убрать, если не требуется)
        # print(final_json)

        # Возврат данных в формате JSON
        return {"final_json": final_json}
    except HTTPException as e:
        error_message = str(e.detail) if hasattr(e, 'detail') else str(e)
        logger.error(f"Error occured get_keys: {error_message}")
        return {"error get_keys": error_message}

    except Exception as e:
        error_message = str(e)
        logger.error(f"Error occurred get_keys: {error_message}")
        return {"error": error_message}
