import json

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from you_tube_module import *
import traceback
import asyncio
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




MAX_RETRIES = 3  # Количество попыток

@app.get("/get_you_tube_by_channel/")
async def create_ideas(channel_name: str):
    """
    Асинхронная функция для создания идей для видео на YouTube по имени канала.

    :param channel_name: Имя канала на YouTube, для которого необходимо создать идеи.
    :return: JSON-объект с идеями для видео или ошибкой, если что-то пошло не так.
    """

    logger.info(f"Received channel_name: {channel_name}")

    for _ in range(MAX_RETRIES):
        try:
            final_json = await general_func(channel_name)

            if not final_json:
                await asyncio.sleep(3)  # Задержка перед повторной попыткой
                raise ValueError("Received empty JSON response")

            return {"final_json": final_json}

        except HTTPException as e:
            error_message = str(e.detail) if hasattr(e, 'detail') else str(e)
            error_traceback = traceback.format_exc()
            full_error_message = f"{error_message}\n{error_traceback}"
            logger.error(f"Error occurred create_ideas: {full_error_message}")
            if _ == MAX_RETRIES - 1:
                return {"error create_ideas": full_error_message}
            await asyncio.sleep(3)

        except Exception as e:
            error_message = str(e) + "\n" + traceback.format_exc()
            logger.error(f"Error occurred create_ideas: {error_message}")
            if _ == MAX_RETRIES - 1:
                return {"error": error_message}
            await asyncio.sleep(3)