from typing import List
from fastapi import APIRouter, Depends
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
async def create_todo(todo: TodoCreate):
    return {
        "id": 1
    }


@router.patch("/{todo_id}")
async def modify_todo(
    *,
    session: Session = Depends(get_session),
    todo_id: int,
    todo: TodoUpdate
):
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
