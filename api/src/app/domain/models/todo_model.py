from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session

from core.config import db_settings

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str


class TodoCreate(SQLModel):
    name: str
    status: str = Field(regex=r"todo|doing|done")


class TodoUpdate(SQLModel):
    name: Optional[str]
    status: Optional[str] = Field(default=None, regex=r"todo|doing|done")


engine = create_engine(db_settings.db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


async def get_session():
    with Session(engine) as session:
        yield session
