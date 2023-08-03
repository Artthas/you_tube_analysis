import { Configuration, OpenAIApi } from 'openai';

export function isYouTubeLink(url: string): boolean {
  const pattern = /^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+/;
  return pattern.test(url);
}

export async function getKeywords(textArray: Array<string>) {
  const configuration = new Configuration({
    apiKey: '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',
  });
  const openai = new OpenAIApi(configuration);

  const text = textArray.join(', ');

  const completion = await openai.createChatCompletion({
    model: "gpt-3.5-turbo",
    messages: [{"role": "system", "content": "You are a helpful assistant."}, {role: "user", content: `Вот мой список заголовков: ${text}. Пожалуйста, выделите 10 ключевых слов из этого списка, которые можно использовать для поиска на YouTube.`}],
  });
  console.log(completion.data.choices[0].message);
}