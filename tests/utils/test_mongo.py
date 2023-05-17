import pytest
from momoai_core import MongoDBClient
from mongomock import MongoClient
from unittest.mock import patch

# Define a fixture for the MongoDB client
@pytest.fixture
def mock_mongo_client():
    with patch('pymongo.MongoClient', new=MongoClient):
        yield

# Define a fixture for the MongoDB client
@pytest.fixture
def db_client(mock_mongo_client):
    client = MongoDBClient()
    yield client
    client.clear_collection('test_collection')  # Clear the collection after each test

def test_insert_data_single(db_client):
    data = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
    db_client.insert_data(data, 'test_collection')
    result = db_client.find_data({}, 'test_collection')
    # Ignore the _id field in comparison
    assert result == [data]

def test_insert_data_multiple(db_client):
    data = [{"_id": 1, "name": "John", "age": 30, "city": "New York"}, {"_id": 2, "name": "Jane", "age": 25, "city": "Los Angeles"}]
    db_client.insert_data(data, 'test_collection')
    result = db_client.find_data({}, 'test_collection')
    # Ignore the _id field in comparison
    assert result == data

def test_update_data(db_client):
    data = {"_id": 1, "name": "John", "age": 30, "city": "New York"}
    db_client.insert_data(data, 'test_collection')
    new_values = {"age": 35}
    db_client.update_data({"_id": 1, "name": "John"}, new_values, 'test_collection')
    result = db_client.find_data({"_id": 1, "name": "John"}, 'test_collection')
    # Ignore the _id field in comparison
    updated_data = {"_id": 1, "name": "John", "age": 35, "city": "New York"}
    assert result == [updated_data]
