from .mongo_database import MongoDatabase
from model.player import Player

players_normalized_collection: str = "players-normalized"
players_collection: str = "players"


class PlayersRepository:

    @staticmethod
    def getAllPlayers() -> list[Player]:
        cursor = MongoDatabase.find(collection=players_normalized_collection, query={})
        players: list[Player] = [Player.from_dict(item) for item in cursor]
        return players

    @staticmethod
    def getAllOringalPlayersValues() -> list[Player]:
        cursor = MongoDatabase.find(collection=players_collection, query={})
        players: list[Player] = [Player.from_dict(item) for item in cursor]
        return players
