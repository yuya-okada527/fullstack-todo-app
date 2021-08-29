from typing import List
from fastapi import APIRouter

from domain.models.todo_model import Todo, TodoCreate, TodoUpdate
from entrypoints.message.todo_message import MutationResponse


router = APIRouter(
    prefix="/v1/todos",
    tags=["TODO"]
)

@router.get(
    "",
    response_model=List[Todo]
)
async def search_todo():
    return [{"id": 1, "name": "name", "status": "todo"}]


@router.post(
    "",
    response_model=MutationResponse
)
async def create_todo(todo: TodoCreate):
    return {
        "id": 1
    }


@router.patch("/{todo_id}")
async def modify_todo(todo_id: int, todo: TodoUpdate):
    return {
        "id": todo_id
    }


@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    return {
        "id": todo_id
    }
