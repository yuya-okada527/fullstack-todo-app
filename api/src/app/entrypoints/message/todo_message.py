from typing import List
from pydantic import BaseModel

from domain.models.todo_model import Todo


class SearchResponse(BaseModel):
    results: List[Todo]
    start: int
    rows: int


class MutationResponse(BaseModel):
    id: int
