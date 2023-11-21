from sklearn.neighbors import KNeighborsClassifier
from .kmeans import Kmeans
from .pca import Pca
from model.player import NewPlayer, Player
from .normalizer import Normalizer
import pandas as pd
from constants.default_values import default_fields
import numpy as np


class Knn:
    knn: KNeighborsClassifier = None

    @staticmethod
    def innitialize():
        knn = KNeighborsClassifier(n_neighbors=5)
        knn.fit(Pca.components_2d_array, Kmeans.labels)
        Knn.knn = knn

    @staticmethod
    def evaluate_new_player(new_player: NewPlayer):
        new_player_normalized = Normalizer.normalize_new_player(new_player=new_player)

        df_new_player = pd.DataFrame([new_player_normalized], columns=default_fields)

        new_player_pca_components = Pca.model.transform(df_new_player)

        distances, indices = Knn.knn.kneighbors(new_player_pca_components)
        new_player_cluster = np.bincount(Kmeans.labels[indices[0]]).argmax()

        algorithms_df = pd.DataFrame({"playerName": [new_player.name],
                                      "steamID": [new_player.steamID],
                                      "cluster": [new_player_cluster],
                                      "pca1": [new_player_pca_components[0][0]],
                                      "pca2": [new_player_pca_components[0][1]]})

        new_player_obj = df_new_player.join(algorithms_df).to_dict("records")

        return new_player_obj[0]
