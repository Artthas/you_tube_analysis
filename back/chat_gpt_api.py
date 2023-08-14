import os
import openai
from aiohttp import ClientSession
import re
from dotenv import load_dotenv
import json
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = key2

def format_keywords(content):
    # Удаляем лишние пробелы и разбиваем строку по запятым или вертикальным чертам
    keywords = re.split(r'\s*[|,]\s*', content.strip())

    # Объединяем ключевые слова с использованием вертикальной черты
    keywords_string = " | ".join(keywords)

    return keywords_string


async def get_keywords(text_array):
    text = ', '.join(text_array)
    print(text)
    # Шаг 1: Получаем описание канала на основе заголовков видео
    description_completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an AI trained to analyze and understand the main theme of a YouTube channel based on its video titles."},
            {"role": "user",
             "content": f"Given the following list of YouTube video titles, can you provide a brief description of the channel's theme and content based on these titles?\n\n{text}"}
        ]
    )
    description = description_completion.choices[0].message['content']
    # Шаг 2: Генерируем ключевые слова на основе полученного описания
    keywords_completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI trained to generate keywords based on a given description."},
            {"role": "user",
             "content": f"Based on this description of a YouTube channel: '{description}', please provide 6 to 8 keywords that would be relevant for searching similar content on YouTube. Return only the keywords, separated by a vertical bar (|), without any additional context."}
        ]
    )
    keywords = keywords_completion.choices[0].message['content']
    print(keywords)
    return {"formatted_keywords": keywords, "first_titles": text}


# async def get_keywords(text_array):
#     text = ', '.join(text_array)
#     print(text)
#     completion = await openai.ChatCompletion.acreate(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are an AI trained to analyze and extract keywords from a list of YouTube video titles. The goal is to understand the main theme of a YouTube channel based on its video titles and provide relevant keywords."},
#             {"role": "user",
#              # "content": f"Based on the following list of YouTube video titles, please provide ONLY 6 or 8 keywords that best represent the overall theme of these titles. Return the keywords separated by a vertical bar (|) without any additional details or explanations. I need just the keywords in a single line:\n\n{text}"
#              "content": f"Given the following list of YouTube video titles, understand the essence and niche of the channel. Based on this understanding, provide 6 to 8 keywords that would be relevant for searching similar content on YouTube. Return only the keywords, separated by a vertical bar (|), without any additional context or listing the titles:\n\n{text}"
#
#              }
#
#         ]
#     )
#     content = completion.choices[0].message['content']
#
#     # Форматируем ключевые слова, чтобы они всегда были разделены вертикальной чертой
#     formatted_keywords = content
#     print('CONTENT===CONTENT===CONTENT===CONTENT===CONTENT===CONTENT===CONTENT===CONTENT===CONTENT===')
#     print(formatted_keywords)
#     return {"formatted_keywords": formatted_keywords, "first_titles": text}


async def create_ideas(titles):
    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative expert skilled in generating video topic ideas."},
            {"role": "user",
             "content": f"Based on the following list of YouTube video titles: {titles}. Suggest other similar topics so we can make other trending videos. We need titles to be suggested directly as well as short description for new videos."
            }
        ]
    )
    content = completion.choices[0].message['content']

    # Разделяем ответ на отдельные идеи по двойным переносам строк
    raw_ideas = [idea.strip() for idea in content.split('\n\n') if idea.strip()]

    # Преобразуем каждую идею в словарь с названием и описанием
    ideas = []
    for idea in raw_ideas:
        if " - " in idea:
            title, description = idea.split(" - ", 1)
            ideas.append({
                "title": title.strip(),
                "description": description.strip()
            })
    print(json.dumps(ideas, indent=4))
    return ideas
