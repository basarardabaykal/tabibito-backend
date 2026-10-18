from fastapi import APIRouter, Depends

from app.schemas.comment import CommentCreate, CommentDelete, CommentUpdate
from app.services.comment import CommentService, get_comment_service

router = APIRouter()


@router.post("/comment")
async def create_comment(
    comment_in: CommentCreate, service: CommentService = Depends(get_comment_service)
):
    await service.create_comment(comment_in)
    return "Successfully created a comment."


@router.get("/comments")
async def read_comments(service: CommentService = Depends(get_comment_service)):
    result = await service.read_comments()

    return result


@router.patch("/comment")
async def update_comment(
    comment_in: CommentUpdate, service: CommentService = Depends(get_comment_service)
):
    await service.update_comment(comment_in)
    return "Successfully updated the comment."


@router.delete("/comment")
async def delete_comment(
    comment_in: CommentDelete, service: CommentService = Depends(get_comment_service)
):
    await service.delete_comment(comment_in)
    return "Successfully deleted the comment."
