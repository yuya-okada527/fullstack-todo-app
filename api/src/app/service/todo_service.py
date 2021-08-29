from typing import List, Optional
from sqlmodel import Session, select

from domain.models.todo_model import Todo, TodoCreate, TodoUpdate

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


def modify_todo_service(
    session: Session,
    todo_id: int,
    todo: TodoUpdate
) -> Optional[int]:
    target = session.get(Todo, todo_id)
    if not target:
        return None
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(target, key, value)
    session.add(target)
    session.commit()
    return todo_id


def delete_todo_service(
    session: Session,
    todo_id: int
) -> Optional[int]:
    target = session.get(Todo, todo_id)
    if not target:
        return None
    session.delete(target)
    session.commit()
    return todo_id