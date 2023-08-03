# import os
# import openai
# openai.api_key = os.getenv("OPENAI_API_KEY")
#
# def get_keywords(text_array):
#   text = ', '.join(text_array)
#
#   completion = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#       {"role": "system", "content": "You are a helpful assistant."},
#       {"role": "user", "content": f"Вот мой список заголовков: {text}. Пожалуйста, выделите 10 ключевых слов из этого списка, которые можно использовать для поиска на YouTube."}
#     ]
#   )
#   print(completion.choices[0].message)

import os
import openai
from aiohttp import ClientSession

openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_keywords(text_array):
    text = ', '.join(text_array)

    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Вот мой список заголовков: {text}. Пожалуйста, выделите 10 ключевых слов из этого списка, которые можно использовать для поиска на YouTube."}
        ]
    )
    print(completion.choices[0].message)

    # В конце вашей программы закройте HTTP-сессию
    openai.session.set(ClientSession())

    await openai.session.get().close()
