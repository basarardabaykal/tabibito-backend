from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter()


@router.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(User))
    return result.all()


@router.post("/users")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(
        email=user.email, created_at=datetime.now(), updated_at=datetime.now()
    )
    db.add(new_user)
    await db.commit()
    return "Succesfully created a user."
