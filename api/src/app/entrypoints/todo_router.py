from fastapi import APIRouter


router = APIRouter(prefix="/v1/todos")


@router.get("")
async def get_todo():
    return ""
