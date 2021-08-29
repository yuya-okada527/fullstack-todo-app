from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from sqlmodel.sql.expression import select

from domain.models.todo_model import Todo, TodoCreate, TodoUpdate, get_session
from entrypoints.message.todo_message import MutationResponse


router = APIRouter(
    prefix="/v1/todos",
    tags=["TODO"]
)

@router.get(
    "",
    response_model=List[Todo]
)
async def search_todo(
    *,
    session: Session = Depends(get_session)
):
    return session.exec(select(Todo)).all()


@router.post(
    "",
    response_model=MutationResponse
)
async def create_todo(
    *,
    session: Session = Depends(get_session),
    todo: TodoCreate
):
    new_todo = Todo.from_orm(todo)
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    return {
        "id": new_todo.id
    }


@router.patch("/{todo_id}")
async def modify_todo(
    *,
    session: Session = Depends(get_session),
    todo_id: int,
    todo: TodoUpdate
):
    target = session.exec(select(Todo).where(Todo.id == todo_id)).first()
    if not target:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(target, key, value)
    session.add(target)
    session.commit()
    return {
        "id": todo_id
    }


@router.delete("/{todo_id}")
async def delete_todo(
    *,
    session: Session = Depends(get_session),
    todo_id: int
):
    return {
        "id": todo_id
    }
