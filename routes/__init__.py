from fastapi import APIRouter
from .players import router as players_router


main_router = APIRouter()

main_router.include_router(players_router, prefix="/players", tags=["players"])


@main_router.get("/")
async def index():
    return {"message": "funciona"}
