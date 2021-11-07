from fastapi import APIRouter, File

from models.speech_recognition import STT
from models.action import Action

router = APIRouter(
    prefix="/speech_recognition",
    tags=["speech"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def speech_recognition(file: bytes = File(...)):
    stt = STT(file)
    text = stt.get_text()
    action = Action(text).get()
    return {"text": text, "action": action}