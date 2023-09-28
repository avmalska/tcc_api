from sklearn.neighbors import KNeighborsClassifier
from .kmeans import Kmeans
from .pca import Pca
from model.player import NewPlayer
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


