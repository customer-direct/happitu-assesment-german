from fastapi import APIRouter

router = APIRouter()


@router.get("/ping", status_code=200)
async def root():
    return {"ping:": "pong"}
