from sklearn import preprocessing
from repository.players import PlayersRepository
import pandas as pd
from constants.default_values import default_fields
from model.player import NewPlayer


class Normalizer:
    scaler: preprocessing.MinMaxScaler = None

    @staticmethod
    def innitialize():
        players = PlayersRepository.getAllOringalPlayersValues()

        df_players = pd.DataFrame(players)[default_fields]

        Normalizer.scaler = preprocessing.MinMaxScaler()
        Normalizer.scaler.fit(df_players)

    @staticmethod
    def normalize_new_player(new_player: NewPlayer):
        df_new_player = pd.DataFrame(new_player.to_df_dict())
        player_scaled = Normalizer.scaler.transform(df_new_player)
        player_normalized = [((x * 9) + 1) for x in player_scaled[0]]
        return player_normalized
