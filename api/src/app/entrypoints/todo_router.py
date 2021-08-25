from fastapi import APIRouter


router = APIRouter(prefix="/v1/todos")


@router.get("")
async def search_todo():
    return ""


@router.post("")
async def create_todo():
    return ""


@router.put("")
async def modify_todo():
    return ""


@router.delete("")
async def delete_todo():
    return ""
