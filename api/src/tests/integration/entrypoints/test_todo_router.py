import json

from fastapi.testclient import TestClient
from sqlmodel import Session
from sqlmodel.sql.expression import select
from domain.models.todo_model import Todo
from tests.utils import TODO_API_PATH


def test_search_todo(client: TestClient, session: Session):
    todo = Todo(name="test", status="todo")
    session.add(todo)
    session.commit()
    session.refresh(todo)

    response = client.get(TODO_API_PATH)
    assert response.status_code == 200
    assert response.json() == {
        "results": [todo],
        "start": 0,
        "rows": 10
    }


def test_create_todo(client: TestClient, session: Session):
    todo = {
        "name": "test",
        "status": "todo"
    }
    response = client.post(TODO_API_PATH, json.dumps(todo))
    assert response.status_code == 200
    assert response.json() == {"id": 1}
    new_todo = session.exec(select(Todo).where(Todo.name == todo["name"])).one()
    assert new_todo.name == todo["name"]
    assert new_todo.status == todo["status"]


def test_modify_todo(client: TestClient, session: Session):
    todo = Todo(name="test", status="todo")
    session.add(todo)
    session.commit()
    session.refresh(todo)
    response = client.patch(TODO_API_PATH + "/" + str(todo.id), json.dumps({
        "status": "doing"
    }))
    assert response.status_code == 200
    assert response.json() == {"id": todo.id}
    session.refresh(todo)
    assert todo.status == "doing"


def test_modify_todo_not_found(client: TestClient):
    response = client.patch(TODO_API_PATH + "/" + "1", json.dumps({}))
    assert response.status_code == 404


def test_delete_todo(client: TestClient, session: Session):
    todo = Todo(name="test", status="todo")
    session.add(todo)
    session.commit()
    session.refresh(todo)
    todo_id = todo.id
    response = client.delete(TODO_API_PATH + "/" + str(todo_id))
    assert response.status_code == 200
    assert response.json() == {"id": todo_id}
    assert session.get(Todo, todo_id) is None


def test_delete_todo_not_found(client: TestClient):
    response = client.delete(TODO_API_PATH + "/" + "1")
    assert response.status_code == 404
