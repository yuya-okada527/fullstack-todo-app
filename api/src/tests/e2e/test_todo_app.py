import json
from fastapi.testclient import TestClient

from tests.utils import TODO_API_PATH

def test_all_scenario(client: TestClient):
    assert client.get(TODO_API_PATH).json()["results"] == []
    client.post(TODO_API_PATH, json.dumps({
        "name": "test",
        "status": "todo"
    }))
    assert client.get(TODO_API_PATH).json()["results"] == [{
        "id": 1,
        "name": "test",
        "status": "todo"
    }]
    client.patch(f"{TODO_API_PATH}/1", json.dumps({
        "status": "doing"
    }))
    assert client.get(TODO_API_PATH).json()["results"] == [{
        "id": 1,
        "name": "test",
        "status": "doing"
    }]
    client.delete(f"{TODO_API_PATH}/1")
    assert client.get(TODO_API_PATH).json()["results"] == []
