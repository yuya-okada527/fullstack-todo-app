from fastapi import FastAPI

from entrypoints import todo_router


app = FastAPI(
    title="Todo API",
    description="タスク管理アプリのためのAPI",
    version="v1"
)

app.include_router(todo_router.router)
