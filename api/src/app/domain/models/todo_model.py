from typing import Optional

from pydantic import BaseModel

from domain.enums.todo_enums import TodoStatus


class TodoModel(BaseModel):
    id: Optional[str]
    name: Optional[str]
    status: Optional[TodoStatus]
