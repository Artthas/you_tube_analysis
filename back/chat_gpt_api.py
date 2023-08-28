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

async def get_description(info_dict: dict):
    logger.info('start crate description')
    top_new = [item['title'] for item in info_dict['top_new_videos']]
    top_pop = [item['title'] for item in info_dict['top_popular_videos']]
    all_top = top_pop + top_new
    text = ', '.join(all_top)
    # print(text)
    # Шаг 1: Получаем описание канала на основе заголовков видео
    description_completion = await openai.ChatCompletion.acreate(
        model="gpt-4",
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
    return description


async def get_keywords(info_dict: dict):
    logger.info('start crate key words')
    description = info_dict['description']
    # Шаг 2: Генерируем ключевые слова на основе полученного описания
    keywords_completion = await openai.ChatCompletion.acreate(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI trained to generate keywords based on a given description."},
            {"role": "user",
             "content": f"Based on this description of a YouTube channel: '{description}', please provide 6 to 8 keywords that would be relevant for searching similar content on YouTube. Return only the keywords, separated by a vertical bar (|), without any additional context."}
        ]
    )
    keywords = keywords_completion.choices[0].message['content']
    return keywords



async def create_ideas(general_ch, comp_ch_list=None):
    MAX_RETRIES = 5
    logger.debug('Starting the create_ideas function.')
    # print('>>>>>>>>>>>>>>>>>>> general channel <<<<<<<<<<<<<<<<<<<<<<<<')
    # print(general_ch)
    # print('>>>>>>>>>>>>>>>>> comp channel <<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # print(comp_ch_list)
    main_channel_titles = list(general_ch.values())[0]
    relevant_competitors = []
    relevant_competitors_str = ""
    # Проверка релевантности видео конкурентов
    for comp_ch in comp_ch_list:
        channel_info = comp_ch[0]
        competitors_titles = channel_info['first_titles']
        print('>>>>>>>>>>>>>>>>> comp channel <<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        # print(competitors_titles)
        # print(type(competitors_titles))
        competitors_description = channel_info['description']
        # print(competitors_description)

        print('>>>>>>>>>>>>>>>>>>> general channel <<<<<<<<<<<<<<<<<<<<<<<<')
        main_channel_titles = list(general_ch.values())[0]
        # print(main_channel_titles)
        relevance_prompt = f"Given the video titles from the main channel {main_channel_titles} and the description of the competitor's channel {competitors_description}, are they relevant in terms of content and theme? Please answer with a simple 'YES' or 'NO'."

        relevance_response = await openai.ChatCompletion.acreate(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert in analyzing content relevance."},
                {"role": "user", "content": relevance_prompt}
            ]
        )
        relevance_answer = relevance_response.choices[0].message['content'].lower()
        time.sleep(2)

        negative_responses = ["no", "not relevant", "not similar", "not alike", "dissimilar", "unrelated"]
        if any(word in relevance_answer for word in negative_responses):
            logger.info(f"Titles from one channel are not relevant.")
            continue

        # relevant_competitors.extend(competitors_titles)
        if competitors_titles not in relevant_competitors_str:
            relevant_competitors_str += competitors_titles

    if not relevant_competitors:
        logger.warning("The competitor's videos are not relevant enough.")

    print('relevant_competitors relevant_competitors relevant_competitors relevant_competitors')
    # print(relevant_competitors_test)
    # print(relevant_competitors)
    style_prompt = f"""
    Instructions for Generating Video Ideas:

    1. Begin by analyzing the main channel titles: {main_channel_titles}.
    2. Deduce the style, mood, content themes, and tone of voice of the main channel.
    3. If the main channel exudes a youthful aura, the generated titles should reflect an energetic and modern tone. If the channel's tone is more serious, the titles should be mature and authoritative.
    4. Use the relevant competitor's titles {relevant_competitors_str} as a source of inspiration, but ensure that the generated titles are original and not mere replicas.
    5. The goal is to generate entirely new video ideas that:
       - Resonate with the main channel's core essence.
       - Seem like a seamless continuation of the main channel's content.
       - Match the mood, theme, and tone of voice of the main channel titles.
    6. For each idea, ensure:
       - The main title is unique and consists of AT LEAST FOUR WORDS.
       - The two alternative titles or synonyms also consist of AT LEAST FOUR WORDS EACH and should be variations or rephrasings of the main title.
       - A short description that aligns with the titles and provides a brief overview of the video's content.

    Structure the response as:
    IDEA:
    Main Title: [Title here with AT LEAST FOUR WORDS]
    Alternative Title 1: [Variation or rephrasing of the main title with AT LEAST FOUR WORDS]
    Alternative Title 2: [Another variation or rephrasing of the main title with AT LEAST FOUR WORDS]
    Description: [Short description that complements the titles]

    Separate each idea with '---'.
    """

    for attempt in range(MAX_RETRIES):
        ideas_response = await openai.ChatCompletion.acreate(
            model="gpt-4",
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




