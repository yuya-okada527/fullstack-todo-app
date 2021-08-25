import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

TODO_API_PATH = "/v1/todos"

TODO_DATA = {"id": "1", "name": "name", "status": "todo"}


def test_search_todo():
    response = client.get(TODO_API_PATH)
    assert response.status_code == 200
    assert response.json() == [TODO_DATA]


def test_post_todo():
    todo = TODO_DATA.copy()
    todo.pop("id")
    response = client.post(TODO_API_PATH, json.dumps(todo))
    assert response.status_code == 200
    assert response.json() == {"id": TODO_DATA["id"]}


def test_modify_todo():
    response = client.put(TODO_API_PATH + "/" + TODO_DATA["id"])
    assert response.status_code == 200
    assert response.json() == {"id": TODO_DATA["id"]}



def test_delete_todo():
    response = client.delete(TODO_API_PATH)
    assert response.status_code == 200