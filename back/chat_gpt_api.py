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


async def find_concurence(dict_with_all_videos, main_channel_name):

    main_description = dict_with_all_videos[main_channel_name]['description']
    main_keys = dict_with_all_videos[main_channel_name]['key_words']
    true_competitors = []
    for key in dict_with_all_videos:

        if key != main_channel_name:
            print(key)
            top_popular_video = [i['title'] for i in dict_with_all_videos[key]['top_popular_videos']]
            top_new_video = [i['title'] for i in dict_with_all_videos[key]['top_new_videos']]
            all_top = top_new_video + top_popular_video
            competitors_titles = '\n'.join(all_top)
            relevance_prompt = f"""
                Instructions for Relevance Check:

                1. You are provided with the main channel description, keywords, and a list of video titles from a competitor's channel.
                2. Main Channel Description: {main_description}
                3. Main Channel Keywords: {main_keys}
                4. Competitor's Video Titles: {competitors_titles}
                5. Analyze the provided description, keywords, and video titles to determine if they are relevant in terms of content and theme.
                6. Criteria for Relevance: If at least 90% of the provided video titles are relevant to the main channel description and keywords, then they are considered relevant.
                7. Expected Response: Provide a response of 'YES' if the criteria for relevance is met. Otherwise, provide a response of 'NO'. Your response should be strictly 'YES' or 'NO'.

                Please provide your response now.
                """

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
            if not any(word in relevance_answer for word in negative_responses):
                true_competitors.append(key)

    return true_competitors

async def create_ideas_by_channal(dict_with_all_videos, main_channel_name, competitors_list):
    MAX_RETRIES = 3
    PAUSE_SECONDS = 2
    main_description = dict_with_all_videos[main_channel_name]['description']
    main_keys = dict_with_all_videos[main_channel_name]['key_words']
    dict_for_ideas = {
        "main_channel": {
            "channel_name": [main_channel_name],
            "top_new": [item['title'] for item in dict_with_all_videos[main_channel_name]['top_new_videos']],
            "top_popular": [item['title'] for item in dict_with_all_videos[main_channel_name]['top_popular_videos']],
            "main_description": main_description,
            "main_keys": main_keys,
            "ideas_by_top_new": [],
            "ideas_by_top_popular": [],
        },
        "concurrent_channels": {
            "channel_name": [],
            "top_new": [],
            "top_popular": [],
            "ideas_by_top_new": [],
            "ideas_by_top_popular": [],
        }
    }

    for comp_name in competitors_list:
        dict_for_ideas["concurrent_channels"]["channel_name"].append(comp_name)
        dict_for_ideas["concurrent_channels"]["top_new"] += [video['title'] for video in dict_with_all_videos[comp_name]['top_new_videos']]
        dict_for_ideas["concurrent_channels"]["top_popular"] += [video['title'] for video in dict_with_all_videos[comp_name]['top_popular_videos']]


    for channel_type, channel_data in dict_for_ideas.items():

        for video_type, video_titles in channel_data.items():
            if video_type in ['top_new', 'top_popular']:
                video_titles_str = '\n'.join(video_titles)

                # Подготовка промпта
                style_prompt = f"""
                Instructions for Generating Video Ideas:

                1. Begin by analyzing the main channel description: {main_description}.
                2. Deduce the style, mood, content themes, and tone of voice of the main channel by analyzing the video titles: {video_titles_str}.
                3. If the main channel exudes a youthful aura, the generated titles should reflect an energetic and modern tone. If the channel's tone is more serious, the titles should be mature and authoritative.
                4. Use the relevant competitor's titles {main_keys} as a source of inspiration, but ensure that the generated titles are original and not mere replicas.
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
                # Попытки генерации идей
                for attempt in range(MAX_RETRIES):
                    logger.info(f"start generate ideas with attempt {attempt}.")
                    ideas_response = await openai.ChatCompletion.acreate(
                        model="gpt-4",
                        messages=[
                            {"role": "system",
                             "content": "You are a creative expert skilled in generating video topic ideas."},
                            {"role": "user", "content": style_prompt}
                        ]
                    )
                    content = ideas_response.choices[0].message['content']
                    # Разделяем ответ на отдельные идеи
                    raw_ideas = [idea.strip() for idea in content.split('---') if idea.strip()]

                    structured_ideas = []
                    for idea in raw_ideas:
                        lines = idea.split("\n")
                        titles = [lines[i].split(": ")[1].strip() for i in range(1, 4)]
                        description = lines[4].split(": ")[1].strip()

                        structured_ideas.append({
                            "Main Title": titles[0],
                            "Alternative Title 1": titles[1],
                            "Alternative Title 2": titles[2],
                            "Description": description
                        })

                    if structured_ideas:
                        logger.info(f"Successfully generated ideas on attempt {attempt}.")
                        # Добавляем сгенерированные идеи в dict_for_ideas
                        ideas_key = f'ideas_by_{video_type}'
                        dict_for_ideas[channel_type][ideas_key] = structured_ideas
                        break
                    # Пауза перед следующей попыткой
                    time.sleep(PAUSE_SECONDS)

    return dict_for_ideas