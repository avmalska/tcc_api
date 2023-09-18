from .mongo_database import MongoDatabase
from model.player import Player


collection: str = "players-normalized"


class PlayersRepository:

    @staticmethod
    def getAllPlayers() -> list[Player]:
        cursor = MongoDatabase.find(collection=collection, query={})
        players: list[Player] = [Player.from_dict(item) for item in cursor]
        return players
