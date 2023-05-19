import os
import pytest
from momoai_core import MongoDBClient
from momoai_core import MongoCollections


# Define a fixture for the MongoDB client
@pytest.fixture
def db_client():
    client = MongoDBClient(
        host=os.environ["MONGO_HOST"],
        port=int(os.environ["MONGO_PORT"]),
        username=os.environ["MONGO_USER"],
        password=os.environ["MONGO_PASSWORD"],
        db_name=os.environ["MONGO_DB_NAME"]
    )
    client.clear_collection(MongoCollections.users)  # Clear the collection after each test
    return client

def test_insert_single(db_client):
    data = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
    db_client.insert(data=data, collection=MongoCollections.users)
    result = db_client.find(collection=MongoCollections.users, query={})
    # Ignore the _id field in comparison
    assert result == [data]

def test_insert_multiple(db_client):
    data = [{"_id": 1, "name": "John", "age": 30, "city": "New York"}, {"_id": 2, "name": "Jane", "age": 25, "city": "Los Angeles"}]
    db_client.insert(data=data, collection=MongoCollections.users)
    result = db_client.find(collection=MongoCollections.users, query={})
    # Ignore the _id field in comparison
    assert result == data

def test_update(db_client):
    data = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
    db_client.insert(data=data, collection=MongoCollections.users)
    new_values = {"age": 35}
    db_client.update(collection=MongoCollections.users, new_values=new_values, query={"_id": 1, "name": "John"})
    result = db_client.find(collection=MongoCollections.users, query={"_id": 1, "name": "John"})
    # Ignore the _id field in comparison
    updated_data = {"_id": 1, "name": "John", "age": 35, "city": "New York"}
    assert result == [updated_data]

def test_cleanup(db_client):
    db_client.clear_collection(MongoCollections.users)
