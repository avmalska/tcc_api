from fastapi import APIRouter
from repository.players import PlayersRepository


router = APIRouter()


@router.get("")
async def get_all_players():
    return [player.to_dict() for player in PlayersRepository.getAllPlayers()]
