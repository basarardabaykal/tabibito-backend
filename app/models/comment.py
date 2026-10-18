from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import AbstractBaseModel

if TYPE_CHECKING:
    from app.models.user import User


class Comment(AbstractBaseModel):
    __tablename__ = "comments"

    content: Mapped[str] = mapped_column(String(1024))
    created_by_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )
    created_by: Mapped["User"] = relationship(back_populates="created_comments")
