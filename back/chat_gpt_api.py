import os
import openai
from aiohttp import ClientSession
import re
from dotenv import load_dotenv

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
    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": f"Вот мой список заголовков: {text}. Пожалуйста, выделите 10 ключевых слов из этого списка, которые можно использовать для поиска на YouTube."}
            {"role": "user",
             "content": f"I will provide you with a list of YouTube video titles. Based on these titles, you need to understand the channel's content and niche and create 3 or 4 keywords to search for the most relevant videos on YouTube and write all the keywords in a single line, separated by a vertical bar (|):\n\n\n\n{text}"}

        ]
    )
    # print(completion.choices[0].message['content'])
    content = completion.choices[0].message['content']

    # Форматируем ключевые слова, чтобы они всегда были разделены вертикальной чертой
    formatted_keywords = format_keywords(content)
    print(f'in gpt logic\n{formatted_keywords}')
    return formatted_keywords
