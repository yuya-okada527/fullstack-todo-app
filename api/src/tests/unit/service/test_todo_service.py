from sqlmodel import Session

from domain.models.todo_model import Todo
from service.todo_service import search_todo_service


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