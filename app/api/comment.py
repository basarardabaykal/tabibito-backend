from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentDelete, CommentUpdate

router = APIRouter()


@router.post("/comment")
async def create_comment(comment: CommentCreate, db: AsyncSession = Depends(get_db)):
    new_comment = Comment(
        content=comment.content,
        created_by_id=comment.created_by_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    db.add(new_comment)
    await db.commit()

    return "Successfully created a comment."


@router.get("/comments")
async def read_comments(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(Comment))

    return (result.all(),)


@router.patch("/comment")
async def update_comment(comment: CommentUpdate, db: AsyncSession = Depends(get_db)):
    comment_to_update = await db.get(Comment, comment.id)
    if not comment_to_update:
        return "No comment with the given id found."

    update_data = comment.model_dump(exclude_defaults=True)
    for key, value in update_data.items():
        setattr(comment_to_update, key, value)

    await db.commit()

    return "Successfully updated the comment."


@router.delete("/comment")
async def delete_comment(comment: CommentDelete, db: AsyncSession = Depends(get_db)):
    comment_to_delete = await db.get(Comment, comment.id)
    if not comment_to_delete:
        return "No comment with the given id found."

    await db.delete(comment_to_delete)
    await db.commit()

    return "Successfully deleted the comment."
