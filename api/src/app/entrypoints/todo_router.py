from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session

from domain.models.todo_model import Todo, TodoCreate, TodoUpdate, get_session
from entrypoints.message.todo_message import MutationResponse
from service.todo_service import search_todo_service


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
    session: Session = Depends(get_session),
    offset: Optional[int] = Query(0),
    limit: Optional[int] = Query(10)
):
    return search_todo_service(
        session=session,
        offset=offset,
        limit=limit
    )


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
    target = session.get(Todo, todo_id)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
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
    target = session.get(Todo, todo_id)
    if not target:
        raise HTTPException(status_code=404, detail="Target not found")
    session.delete(target)
    session.commit()
    return {
        "id": todo_id
    }
