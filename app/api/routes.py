from fastapi import APIRouter
from app.services.news_service import fetch_news
from app.services.llm_service import summarize_text

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API Working"}

@router.get("/news")
def get_news(topic: str = "technology"):

    return fetch_news(topic)

@router.post("/summarize")
def summarize(data: dict):

    text = data.get("text")

    summary = summarize_text(text)

    return {
        "summary": summary
    }