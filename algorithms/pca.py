from sklearn.decomposition import PCA
from repository.players import PlayersRepository
import pandas as pd
from constants.default_values import default_fields
from typing import TypedDict


class PcaComponents(TypedDict):
    x: list[float]
    y: list[float]


class Pca:
    model: PCA = None
    principal_components: PcaComponents = None
    components_2d_array: list[list[float]] = None

    @staticmethod
    def innitialize():
        df = pd.DataFrame(PlayersRepository.getAllPlayers())[default_fields]

        Pca.model = PCA(n_components=2)
        Pca.model.fit(df)
        pca_transform = Pca.model.transform(df)
        Pca.components_2d_array = pca_transform
        Pca.principal_components = {"x": pca_transform[:, 0], "y": pca_transform[:, 1]}
