from groq import Groq
from app.core.config import GROQ_API_KEY
from app.services.news_service import fetch_news, detect_category
from app.services.semantic_router import detect_domain_semantic

client = Groq(api_key=GROQ_API_KEY)


def ask_llm(prompt: str):

    # Detect category
    category = detect_domain_semantic(prompt)

    # Fetch news
    news_data = fetch_news(category)

    final_prompt = f"""
You are an AI news assistant.

User query:
{prompt}

Latest news:
{news_data}

Summarize the important updates clearly.
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )

    return completion.choices[0].message.content