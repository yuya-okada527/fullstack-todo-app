from sqlmodel import Session

from domain.models.todo_model import Todo, TodoCreate, TodoUpdate
from service.todo_service import create_todo_service, delete_todo_service, modify_todo_service, search_todo_service


def test_search_todo_service(session: Session):
    todo = Todo(name="test", status="todo")
    session.add(todo)
    session.commit()
    session.refresh(todo)

    assert search_todo_service(session, 0, 10) == [todo]


def test_search_todo_searvice_pagination(session: Session):
    todos = [
        Todo(name="test1", status="todo"),
        Todo(name="test2", status="todo"),
        Todo(name="test3", status="todo")
    ]
    for todo in todos:
        session.add(todo)
    session.commit()
    for todo in todos:
        session.refresh(todo)

    assert search_todo_service(session, 0, 2) == [
        todos[0],
        todos[1]
    ]
    assert search_todo_service(session, 2, 2) == [
        todos[2]
    ]


def test_create_todo_service(session: Session):
    assert create_todo_service(session, TodoCreate(name="test", status="todo")) == 1


def test_delete_todo_service(session: Session):
    todo = Todo(name="test", status="todo")
    session.add(todo)
    session.commit()
    session.refresh(todo)
    todo_id = todo.id
    delete_todo_service(session, todo_id)
    assert session.get(Todo, todo_id) is None