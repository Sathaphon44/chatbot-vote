from app.config import Config
from pymongo import MongoClient
class MongoDatabase:
    def connect(self, database):
        connect = MongoClient(Config.MONGO_URI)
        db = connect[database]
        return db