import pandas as pd
from fastapi import APIRouter
from repository.players import PlayersRepository
from algorithms.kmeans import Kmeans
from algorithms.pca import Pca

router = APIRouter()


@router.get("")
async def get_all_players():
    players_df = pd.DataFrame(PlayersRepository.getAllPlayers())
    algorithms_df = pd.DataFrame({"cluster": Kmeans.labels,
                                  "pca1": Pca.principal_components["x"],
                                  "pca2": Pca.principal_components["y"]})

    return players_df.join(algorithms_df).to_dict("records")


@router.post("/kmeans")
async def get_kmeans_labels(campos_kmeans: list[str]):
    return Kmeans.calculate_kmeans(campos_kmeans)


@router.post("/pca")
async def get_pca_labels():
    return True
