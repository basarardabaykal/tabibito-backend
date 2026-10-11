from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import AbstractBaseModel

if TYPE_CHECKING:
    from app.models.comment import Comment
    from app.models.entry import Entry


class User(AbstractBaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_entries: Mapped[list[Entry]] = relationship(
        "Entry", back_populates="created_by"
    )
    created_comments: Mapped[list[Comment]] = relationship(
        "Comment", back_populates="created_by"
    )
