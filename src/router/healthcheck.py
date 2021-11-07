from fastapi import APIRouter, Request

from models.action import Action

router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def healthcheck():
    return {"status": "ok"}
