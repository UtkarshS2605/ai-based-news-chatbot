from fastapi import APIRouter, Query
from app.services.llm_service import ask_llm
from fastapi import Form
from fastapi.responses import PlainTextResponse

router = APIRouter()

@router.post("/chat")
def chat(prompt: str = Query(...)):
    try:
        response = ask_llm(prompt)
        return {"response": response}
    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
    
@router.post("/webhook")
def whatsapp_webhook(Body: str = Form(...)):
    response = ask_llm(Body)
    return PlainTextResponse(response)