from sklearn.cluster import KMeans
from repository.players import PlayersRepository
import pandas as pd

campos_kmeans_default = ["kdr", "kpr", "awpKpr", "adr", "aud", "kast",
                         "multiKills", "openingRatio", "clutchesRatio", "flashTimeMean", "rating"]


class Kmeans:
    kmeans: KMeans = None
    kmeans_labels: dict = None

    @staticmethod
    def calculate_kmeans(campos_kmeans: list[str] = None):
        if campos_kmeans is None:
            campos_kmeans = [x for x in campos_kmeans_default]
        players_df_completo = pd.DataFrame(PlayersRepository.getAllPlayers())
        players_df = players_df_completo[campos_kmeans]
        kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10, random_state=0)
        kmeans.fit(players_df)
        kmeans_labels_normalized = {str(x): [] for x in range(5)}
        for index, cluster in enumerate(kmeans.labels_):
            kmeans_labels_normalized[str(cluster)].append((players_df_completo.iloc[index, 0]))
        Kmeans.kmeans = kmeans
        Kmeans.kmeans_labels = kmeans_labels_normalized
        return kmeans_labels_normalized
