from fastapi import APIRouter, Depends

from app.schemas.user import UserCreate
from app.services.user import UserService, get_user_service

router = APIRouter()


@router.get("/users")
async def read_users(service: UserService = Depends(get_user_service)):
    result = await service.read_users()

    return result


@router.post("/users")
async def create_user(
    user_in: UserCreate, service: UserService = Depends(get_user_service)
):
    await service.create_user(user_in)
    return "Succesfully created a user."
