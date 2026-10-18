from datetime import datetime

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.results import DetailedResult
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def read_users(self):
        result = await self.db.scalars(select(User))
        return DetailedResult[list[User]](
            is_successful=True,
            message="Successfully retrieved all users.",
            data=list(result.all()),
        )

    async def create_user(self, user_in: UserCreate):
        new_user = User(
            email=user_in.email, created_at=datetime.now(), updated_at=datetime.now()
        )
        self.db.add(new_user)
        await self.db.commit()


def get_user_service(db: AsyncSession = Depends(get_db)):
    return UserService(db)
