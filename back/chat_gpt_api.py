import os
import time
import logging
import openai
from aiohttp import ClientSession
import re
from dotenv import load_dotenv
import json
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = key2
# Инициализация логгера
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



def format_keywords(content):
    # Удаляем лишние пробелы и разбиваем строку по запятым или вертикальным чертам
    keywords = re.split(r'\s*[|,]\s*', content.strip())

    # Объединяем ключевые слова с использованием вертикальной черты
    keywords_string = " | ".join(keywords)

    return keywords_string


async def get_keywords(text_array):
    text = ', '.join(text_array)
    # print(text)
    # Шаг 1: Получаем описание канала на основе заголовков видео
    description_completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an AI trained to analyze and understand the main theme of a YouTube channel based on its video titles."},
            {
                "role": "user",
                "content": f"Given the following list of YouTube video titles, can you provide a detailed and precise description of the channel's main theme, its target audience, and the type of content it primarily focuses on?\n\nFor example, if the titles were mostly about cooking, the description should mention that the channel is a cooking channel, targeting food enthusiasts, and primarily focuses on recipes, cooking techniques, etc.\n\nVideo Titles:\n\n{text}"
            }
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
    return {"formatted_keywords": keywords, "first_titles": text, 'description': description}



async def create_ideas(general_ch, comp_ch_list=None):
    MAX_RETRIES = 5
    logger.debug('Starting the create_ideas function.')
    # print('>>>>>>>>>>>>>>>>>>> general channel <<<<<<<<<<<<<<<<<<<<<<<<')
    # print(general_ch)
    # print('>>>>>>>>>>>>>>>>> comp channel <<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # print(comp_ch_list)
    main_channel_titles = list(general_ch.values())[0]
    relevant_competitors = []
    # Проверка релевантности видео конкурентов
    for comp_ch in comp_ch_list:
        main_channel_titles = list(general_ch.values())[0]
        competitor_channel_name = list(comp_ch.keys())[0]
        competitor_titles = ', '.join(comp_ch[competitor_channel_name])

        relevance_prompt = f"Given the video titles from the main channel {main_channel_titles} and the competitor's titles {competitor_titles}, are they relevant in terms of content and theme? Please answer with a simple 'YES' or 'NO'."

        relevance_response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in analyzing content relevance."},
                {"role": "user", "content": relevance_prompt}
            ]
        )
        relevance_answer = relevance_response.choices[0].message['content'].lower()
        # print('relevant answer')
        # print(relevance_answer)
        # print(main_channel_titles)
        # print('********')
        # print(competitor_titles)
        time.sleep(2)

        negative_responses = ["no", "not relevant", "not similar", "not alike", "dissimilar", "unrelated"]
        if any(word in relevance_answer for word in negative_responses):
            logger.info(f"Titles from {competitor_channel_name} are not relevant.")

            continue

        relevant_competitors.extend(comp_ch[competitor_channel_name])

    if not relevant_competitors:
        logger.warning("The competitor's videos are not relevant enough.")

    style_prompt = f"""
    Algorithm for Generating Video Ideas:

    1. Analyze the main channel titles: {main_channel_titles}.
    2. Understand the style, mood, content themes, and tone of voice of the main channel.
    3. If the main channel has a youthful vibe, maintain a similar energetic and modern tone. If it's more serious, keep the tone mature and authoritative.
    4. If available, consider the relevant competitor's titles {', '.join(relevant_competitors)} for inspiration, but DO NOT replicate them.
    5. Generate entirely new video ideas that:
       - Align closely with the main channel's essence.
       - Feel like a natural extension of the main channel's content.
       - Have a similar mood, theme, and tone of voice as the main channel titles.
    6. For each idea, provide:
       - Three title options.
       - A short description.

    Structure the response as:
    IDEA:
    Title Option 1: [Title here]
    Title Option 2: [Title here]
    Title Option 3: [Title here]
    Description: [Short description here]

    Separate each idea with '---'.
    """

    for attempt in range(MAX_RETRIES):
        ideas_response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative expert skilled in generating video topic ideas."},
                {"role": "user", "content": style_prompt}
            ]
        )
        content = ideas_response.choices[0].message['content']
        print(f">>>>>>>>>>>>>>>>>>> RAW CONTENT attempt {attempt} <<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        # print(content)
        # Разделяем ответ на отдельные идеи
        raw_ideas = [idea.strip() for idea in content.split('---') if idea.strip()]

        structured_ideas = {}
        for idx, idea in enumerate(raw_ideas, 1):
            lines = idea.split("\n")
            titles = [lines[i].split(": ")[1].strip() for i in range(1, 4)]
            description = lines[4].split(": ")[1].strip()

            structured_ideas[f"Idea {idx}"] = {
                "titles": titles,
                "description": description
            }

        if structured_ideas:
            logger.info(f"Successfully generated ideas on attempt {attempt}.")

            return structured_ideas

    logger.error("Failed to generate ideas after multiple attempts.")
    return {"error": "Failed to generate ideas after multiple attempts."}




