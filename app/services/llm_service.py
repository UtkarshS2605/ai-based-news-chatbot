from groq import Groq
from app.core.config import GROQ_API_KEY
from app.services.news_service import fetch_news, detect_category

client = Groq(api_key=GROQ_API_KEY)

def detect_category(prompt: str):
    prompt = prompt.lower()

    if "ai" in prompt or "tech" in prompt or "technology" in prompt:
        return "technology"
    elif "finance" in prompt or "business" in prompt or "stock" in prompt:
        return "business"
    elif "sports" in prompt or "cricket" in prompt or "football" in prompt:
        return "sports"
    elif "crypto" in prompt or "bitcoin" in prompt:
        return "cryptocurrency"
    elif "health" in prompt or "medicine" in prompt:
        return "health"
    else:
        return prompt

def ask_llm(prompt: str):

    # Detect category
    category = detect_category(prompt)

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