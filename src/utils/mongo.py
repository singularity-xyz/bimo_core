import os
from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, host=None, port=None, user=None, password=None, db_name='momoai'):
        host = host if host is not None else os.getenv('MONGO_HOST', 'localhost')
        port = port if port is not None else int(os.getenv('MONGO_PORT', 27017))
        user = user if user is not None else os.getenv('MONGO_USER')
        password = password if password is not None else os.getenv('MONGO_PASSWORD')
        self.client = MongoClient(host, port, username=user, password=password)
        self.db = self.client[db_name]

    def insert_data(self, data, collection_name='your_collection'):
        if isinstance(data, dict):
            self.db[collection_name].insert_one(data)
        elif isinstance(data, list):
            self.db[collection_name].insert_many(data)
        else:
            raise TypeError("Data should be either a dictionary (for one document) or a list (for multiple documents)")

    def find_data(self, query={}, collection_name='your_collection'):
        results = self.db[collection_name].find(query)
        return [result for result in results]

    def update_data(self, query, new_values, collection_name='your_collection'):
        self.db[collection_name].update_many(query, {"$set": new_values})

    def clear_collection(self, collection_name='your_collection'):
        self.db[collection_name].delete_many({})
