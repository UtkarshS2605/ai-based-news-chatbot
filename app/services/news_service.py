import requests
from app.core.config import NEWS_API_KEY

def detect_category(prompt: str):
    prompt = prompt.lower()

    domains = {
        "ai": "artificial intelligence",
        "tech": "technology",
        "technology": "technology",
        "startup": "startups",
        "business": "business",
        "finance": "finance",
        "crypto": "cryptocurrency",
        "sports": "sports",
        "health": "health",
        "politics": "politics",
        "science": "science",
        "climate": "climate"
    }

    for key, value in domains.items():
        if key in prompt:
            return value

    return prompt


# Fetch latest news
def fetch_news(query: str):
    url = "https://newsapi.org/v2/everything"

    params = {
        "q": query,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": NEWS_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            return "No recent news found."

        news_text = ""

        for i, article in enumerate(articles, 1):
            title = article.get("title", "No title available")
            description = article.get("description", "No description available.")
            url = article.get("url", "")

            news_text += f"{i}. {title}\n"
            news_text += f"{description}\n"
            news_text += f"{url}\n\n"

        return news_text

    except Exception as e:
        return f"Error fetching news: {str(e)}"