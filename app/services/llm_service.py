from openai import OpenAI

from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def summarize_text(text):

    try:

        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {
                    "role": "system",
                    "content": "You are a helpful news summarizer."
                },

                {
                    "role": "user",
                    "content": f"Summarize this news article simply:\n\n{text}"
                }

            ],

            temperature=0.5,
            max_tokens=200

        )

        return response.choices[0].message.content

    except Exception as e:

        return str(e)