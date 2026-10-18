from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CommentCreate(BaseModel):
    content: str
    created_by_id: int
    created_at: datetime
    updated_at: datetime


class CommentUpdate(BaseModel):
    id: int
    content: Optional[str] = None


class CommentDelete(BaseModel):
    id: int
