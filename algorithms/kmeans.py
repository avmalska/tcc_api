from sklearn.cluster import KMeans
from repository.players import PlayersRepository
import pandas as pd


class Kmeans:
    campos_kmeans = ["kdr", "kpr", "awpKpr", "adr", "aud", "kast",
                     "multiKills", "openingRatio", "clutchesRatio", "flashTimeMean", "rating"]
    kmeans: KMeans = None

    @staticmethod
    def initialize():
        players_df_completo = pd.DataFrame(PlayersRepository.getAllPlayers())
        players_df = players_df_completo[Kmeans.campos_kmeans]
        Kmeans.kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=0).fit(players_df)
        print(Kmeans.kmeans)
