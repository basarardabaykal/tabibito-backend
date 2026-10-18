from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class EntryCreate(BaseModel):
    title: str
    content: str
    created_by_id: int
    created_at: datetime
    updated_at: datetime


class EntryUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    content: Optional[str] = None


class EntryDelete(BaseModel):
    id: int
