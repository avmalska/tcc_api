from pymongo import MongoClient
from pymongo.database import Database


class MongoDatabase(object):
    URI: str = "mongodb://127.0.0.1:27017"
    DATABASE: Database = None

    @staticmethod
    def initialize():
        client = MongoClient(MongoDatabase.URI)
        MongoDatabase.DATABASE = client["tcc"]

    @staticmethod
    def find(collection: str, query: dict):
        return MongoDatabase.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: dict):
        return MongoDatabase.DATABASE[collection].find_one(query)
