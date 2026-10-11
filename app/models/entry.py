from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import AbstractBaseModel

if TYPE_CHECKING:
    from app.models.user import User


class Entry(AbstractBaseModel):
    __tablename__ = "entries"

    title: Mapped[str] = mapped_column(String(256))
    content: Mapped[str] = mapped_column(Text)
    created_by_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )
    created_by: Mapped["User"] = relationship(back_populates="created_entries")
