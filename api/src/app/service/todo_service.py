from typing import List, Optional
from sqlmodel import Session, select

from domain.models.todo_model import Todo

def search_todo_service(
    session: Session,
    offset: int,
    limit: int
) -> List[Todo]:
    statement = select(Todo).offset(offset).limit(limit)
    return session.exec(statement).all()