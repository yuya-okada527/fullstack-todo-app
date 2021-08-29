from typing import Optional
from pydantic import BaseModel


class MutationResponse(BaseModel):
    id: int
