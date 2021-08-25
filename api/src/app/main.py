from fastapi import FastAPI

from entrypoints import todo_router


app = FastAPI()

app.include_router(todo_router.router)
