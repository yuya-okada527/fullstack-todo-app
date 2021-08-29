from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session

from domain.models.todo_model import Todo, TodoCreate, TodoUpdate, get_session
from entrypoints.message.todo_message import MutationResponse, SearchResponse
from service.todo_service import create_todo_service, delete_todo_service, modify_todo_service, search_todo_service


router = APIRouter(
    prefix="/v1/todos",
    tags=["TODO"]
)

@router.get(
    "",
    response_model=SearchResponse
)
async def search_todo(
    *,
    session: Session = Depends(get_session),
    start: Optional[int] = Query(0, ge=0),
    rows: Optional[int] = Query(10, ge=0, le=100)
):
    todos = search_todo_service(
        session=session,
        offset=start,
        limit=rows
    )
    return {
        "start": start,
        "rows": rows,
        "results": todos
    }


@router.post(
    "",
    response_model=MutationResponse
)
async def create_todo(
    *,
    session: Session = Depends(get_session),
    todo: TodoCreate
):
    todo_id = create_todo_service(
        session=session,
        todo=todo
    )
    return {
        "id": todo_id
    }


@router.patch(
    "/{todo_id}",
    response_model=MutationResponse
)
async def modify_todo(
    *,
    session: Session = Depends(get_session),
    todo_id: int,
    todo: TodoUpdate
):
    target_id = modify_todo_service(
        session=session,
        todo_id=todo_id,
        todo=todo
    )
    if not target_id:
        raise HTTPException(status_code=404, detail="Target not found")
    return {
        "id": target_id
    }


@router.delete(
    "/{todo_id}",
    response_model=MutationResponse
)
async def delete_todo(
    *,
    session: Session = Depends(get_session),
    todo_id: int
):
    target_id = delete_todo_service(session=session, todo_id=todo_id)
    if not target_id:
        raise HTTPException(status_code=404, detail="Target not found")
    return {
        "id": target_id
    }
