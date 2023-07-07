from typing import Mapping
from bimo_core.src.utils import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

# immutable collections dictionary
class MongoCollections:
    users = "Users"
    documents = "Documents"


class MongoDBClient:
    def __init__(self, host=None, port=None, username=None, password=None, db_name=None):
        try:
            # Create a MongoClient object and connect to the MongoDB server
            self.client = MongoClient(host, port, username=username, password=password)
            self.db = self.client[db_name]

        except ConnectionFailure as e:
            # Handle the ConnectionFailure exception
            logging.error(f"Connection to MongoDB failed: {e}")

        logging.info(f"Successfully connected to MongoDB client: {self.client}.")

    def insert(self, data, collection):
        try:
            if isinstance(data, dict):
                self.db[collection].insert_one(data)
            elif isinstance(data, list):
                self.db[collection].insert_many(data)
            else:
                raise TypeError("Data should be either a dictionary (for one document) or a list (for multiple documents)")

        except OperationFailure as e:
            # Handle the OperationFailure exception
            logging.error(f"Insert operation failed: {e}")

    def find(self, collection, query={}):
        try:
            results = self.db[collection].find(query)
            return [result for result in results]

        except OperationFailure as e:
            # Handle the OperationFailure exception
            logging.error(f"Find operation failed: {e}")

    def update(self, collection, new_values, query={}):
        try:
            self.db[collection].update_many(query, {"$set": new_values})

        except OperationFailure as e:
            # Handle the OperationFailure exception
            logging.error(f"Update operation failed: {e}")

    def clear_collection(self, collection):
        try:
            self.db[collection].delete_many({})

        except OperationFailure as e:
            # Handle the OperationFailure exception
            logging.error(f"Delete operation failed: {e}")

