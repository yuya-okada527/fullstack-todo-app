from typing import List, Optional
from sqlmodel import Session, select

from domain.models.todo_model import Todo, TodoCreate

def search_todo_service(
    session: Session,
    offset: int,
    limit: int
) -> List[Todo]:
    statement = select(Todo).offset(offset).limit(limit)
    return session.exec(statement).all()


def create_todo_service(
    session: Session,
    todo: TodoCreate
) -> int:
    new_todo = Todo.from_orm(todo)
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    return new_todo.id
