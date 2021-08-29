from typing import Optional
from sqlmodel import SQLModel, Field

class Todo(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str


class TodoCreate(SQLModel):
    name: str
    status: str


class TodoUpdate(SQLModel):
    name: Optional[str]
    status: Optional[str]
