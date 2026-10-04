from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class AbstractBaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
