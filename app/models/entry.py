from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import AbstractBaseModel


class Entry(AbstractBaseModel):
    __tablename__ = "entries"

    title: Mapped[str] = mapped_column(String(256))
    content: Mapped[str] = mapped_column(Text)
