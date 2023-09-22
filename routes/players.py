from fastapi import APIRouter
from repository.players import PlayersRepository
from algorithms.kmeans import Kmeans

router = APIRouter()


@router.get("")
async def get_all_players():
    return [player.to_dict() for player in PlayersRepository.getAllPlayers()]


@router.post("/kmeans")
async def get_kmeans_labels(campos_kmeans: list[str]):
    return Kmeans.calculate_kmeans(campos_kmeans)


@router.post("/pca")
async def get_pca_labels():
    return True