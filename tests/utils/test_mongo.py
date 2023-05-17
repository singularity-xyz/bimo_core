import os
import pytest
from momoai_core import MongoDBClient


# Define a fixture for the MongoDB client
@pytest.fixture
def db_client():
    client = MongoDBClient(host=os.environ["MONGO_HOST"], port=int(os.environ["MONGO_PORT"]), username=os.environ["MONGO_USER"], password=os.environ["MONGO_PASSWORD"], db_name="momoai")
    client.clear_collection('test_collection')  # Clear the collection after each test
    return client

def test_insert_single(db_client):
    data = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
    db_client.insert(data=data, collection='test_collection')
    result = db_client.find(collection='test_collection', query={})
    # Ignore the _id field in comparison
    assert result == [data]

def test_insert_multiple(db_client):
    data = [{"_id": 1, "name": "John", "age": 30, "city": "New York"}, {"_id": 2, "name": "Jane", "age": 25, "city": "Los Angeles"}]
    db_client.insert(data=data, collection='test_collection')
    result = db_client.find(collection='test_collection', query={})
    # Ignore the _id field in comparison
    assert result == data

def test_update(db_client):
    data = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
    db_client.insert(data=data, collection='test_collection')
    new_values = {"age": 35}
    db_client.update(collection='test_collection', new_values=new_values, query={"_id": 1, "name": "John"})
    result = db_client.find(collection='test_collection', query={"_id": 1, "name": "John"})
    # Ignore the _id field in comparison
    updated_data = {"_id": 1, "name": "John", "age": 35, "city": "New York"}
    assert result == [updated_data]
