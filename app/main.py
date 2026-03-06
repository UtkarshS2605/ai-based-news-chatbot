from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Free AI ChatBot")

app.include_router(router)