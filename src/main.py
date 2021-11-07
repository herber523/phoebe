from fastapi import FastAPI

from router import speech_recognition
from router import action
from router import healthcheck

app = FastAPI()
app.include_router(speech_recognition.router)
app.include_router(action.router)
app.include_router(healthcheck.router)