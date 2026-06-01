import requests

from app.core.config import NEWS_API_KEY


def fetch_news(topic="technology"):

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"category={topic}&"
        f"country=us&"
        f"pageSize=12&"
        f"apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = []

    for article in data.get("articles", []):

        if not article.get("title"):
            continue

        if not article.get("urlToImage"):
            continue

        articles.append({

            "title": article.get("title"),

            "description": article.get("description"),

            "source": article.get("source", {}).get("name"),

            "url": article.get("url"),

            "image": article.get("urlToImage")

        })

    return articles