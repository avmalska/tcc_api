from sklearn.decomposition import PCA
from repository.players import PlayersRepository
import pandas as pd

campos_pca_default = ["kdr", "kpr", "awpKpr", "adr", "aud", "kast",
                      "multiKills", "openingRatio", "clutchesRatio", "flashTimeMean", "rating"]


class Pca:
    pca: PCA = None

    @staticmethod
    def innitialize():
        df = pd.DataFrame(PlayersRepository.getAllPlayers())[campos_pca_default]

        Pca.pca = PCA(n_components=2)
        Pca.pca.fit(df)
