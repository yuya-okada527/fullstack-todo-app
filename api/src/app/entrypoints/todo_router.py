from typing import List
from fastapi import APIRouter

from domain.models.todo_model import TodoModel
from entrypoints.message.todo_message import MutationResponse


router = APIRouter(prefix="/v1/todos")

# TODO messageは、モデルから切り分ける


@router.get(
    "",
    response_model=List[TodoModel]
)
async def search_todo():
    return [{"id": 1, "name": "name", "status": "todo"}]


@router.post(
    "",
    response_model=MutationResponse
)
async def create_todo(todo: TodoModel):
    return {
        "id": "1"
    }


@router.put("/{todo_id}")
async def modify_todo(todo_id: str):
    return {
        "id": todo_id
    }


@router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
    return {
        "id": todo_id
    }
