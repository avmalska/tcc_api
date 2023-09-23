from sklearn.cluster import KMeans
from repository.players import PlayersRepository
import pandas as pd
from constants.default_values import default_fields


class Kmeans:
    kmeans: KMeans = None
    leabels_dictionary: dict = None
    labels: list[int] = None

    @staticmethod
    def calculate_kmeans(campos_kmeans: list[str] = None):
        n_clusters = 5
        if campos_kmeans is None:
            campos_kmeans = [x for x in default_fields]
        players_df_completo = pd.DataFrame(PlayersRepository.getAllPlayers())
        players_df = players_df_completo[campos_kmeans]
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, random_state=0)
        kmeans.fit(players_df)
        Kmeans.labels = kmeans.labels_
        kmeans_labels_normalized = {str(x): [] for x in range(n_clusters)}
        for index, cluster in enumerate(kmeans.labels_):
            kmeans_labels_normalized[str(cluster)].append((players_df_completo.iloc[index, 0]))
        Kmeans.kmeans = kmeans
        Kmeans.leabels_dictionary = kmeans_labels_normalized
        return kmeans_labels_normalized
