import json

from fastapi.testclient import TestClient
from sqlmodel import Session
from domain.models.todo_model import Todo

TODO_API_PATH = "/v1/todos"

TODO_DATA = {"id": 1, "name": "name", "status": "todo"}


def test_search_todo(client: TestClient, session: Session):
    todo = Todo(name="test", status="todo")
    session.add(todo)
    session.commit()
    session.refresh(todo)

    response = client.get(TODO_API_PATH)
    assert response.status_code == 200
    assert response.json() == [todo]


def test_post_todo(client: TestClient, session: Session):
    todo = TODO_DATA.copy()
    todo.pop("id")
    response = client.post(TODO_API_PATH, json.dumps(todo))
    assert response.status_code == 200
    assert response.json() == {"id": TODO_DATA["id"]}


def test_modify_todo(client: TestClient, session: Session):
    response = client.patch(TODO_API_PATH + "/" + str(TODO_DATA["id"]), json.dumps({}))
    assert response.status_code == 200
    assert response.json() == {"id": TODO_DATA["id"]}



def test_delete_todo(client: TestClient, session: Session):
    response = client.delete(TODO_API_PATH + "/" + str(TODO_DATA["id"]))
    assert response.status_code == 200
    assert response.json() == {"id": TODO_DATA["id"]}