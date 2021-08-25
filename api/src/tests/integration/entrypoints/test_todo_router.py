from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

TODO_API_PATH = "/v1/todos"


def test_search_todo():
    response = client.get(TODO_API_PATH)
    assert response.status_code == 200


def test_post_todo():
    response = client.post(TODO_API_PATH)
    assert response.status_code == 200


def test_modify_todo():
    response = client.put(TODO_API_PATH)
    assert response.status_code == 200


def test_delete_todo():
    response = client.delete(TODO_API_PATH)
    assert response.status_code == 200