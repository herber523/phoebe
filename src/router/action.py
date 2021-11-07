from fastapi import APIRouter, Request

from models.action import Action

router = APIRouter(
    prefix="/action",
    tags=["speech"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def action(request: Request):
    json = await request.json()
    text = json.get('text')
    action = Action(text).get()
    return action
