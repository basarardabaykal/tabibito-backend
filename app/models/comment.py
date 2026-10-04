from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import AbstractBaseModel


class Comment(AbstractBaseModel):
    __tablename__ = "comments"

    content: Mapped[str] = mapped_column(String(1024))
