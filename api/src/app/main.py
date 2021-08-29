from fastapi import FastAPI

from entrypoints import todo_router

from domain.models.todo_model import create_db_and_tables


app = FastAPI(
    title="Todo API",
    description="タスク管理アプリのためのAPI",
    version="v1"
)

app.include_router(todo_router.router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
