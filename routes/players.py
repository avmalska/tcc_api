import pandas as pd
from fastapi import APIRouter
from repository.players import PlayersRepository
from algorithms.kmeans import Kmeans
from algorithms.pca import Pca
from algorithms.knn import Knn
from model.player import NewPlayerIncoming, NewPlayer

router = APIRouter()


@router.get("")
async def get_all_players():
    players_df = pd.DataFrame(PlayersRepository.getAllPlayers())
    algorithms_df = pd.DataFrame({"cluster": Kmeans.labels,
                                  "pca1": Pca.principal_components["x"],
                                  "pca2": Pca.principal_components["y"]})

    return players_df.join(algorithms_df).to_dict("records")


@router.post("/eval")
async def evaluate_new_player(new_player_incoming: NewPlayerIncoming):
    new_player = NewPlayer.from_incoming(new_player_incoming)
    new_player_cluster = Knn.evaluate_new_player(new_player)
    return new_player_cluster

