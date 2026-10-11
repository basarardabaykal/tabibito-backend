from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import AbstractBaseModel


class User(AbstractBaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
