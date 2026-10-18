from datetime import datetime

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.results import DetailedResult
from app.db.session import get_db
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentDelete, CommentUpdate


class CommentService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_comment(self, comment_in: CommentCreate):
        new_comment = Comment(
            content=comment_in.content,
            created_by_id=comment_in.created_by_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        self.db.add(new_comment)
        await self.db.commit()

    async def read_comments(self):
        result = await self.db.scalars(select(Comment))

        return DetailedResult[list[Comment]](
            is_successful=True,
            message="Successfully retrieved all comments.",
            data=list(result.all()),
        )

    async def update_comment(self, comment_in: CommentUpdate):
        comment_to_update = await self.db.get(Comment, comment_in.id)
        if not comment_to_update:
            return DetailedResult[None](
                is_successful=False, message="No comment with the given id found."
            )

        update_data = comment_in.model_dump(exclude_defaults=True)
        for key, value in update_data.items():
            setattr(comment_to_update, key, value)

        await self.db.commit()

    async def delete_comment(self, comment_in: CommentDelete):
        comment_to_delete = await self.db.get(Comment, comment_in.id)
        if not comment_to_delete:
            return DetailedResult[None](
                is_successful=False, message="No comment with the given id found."
            )

        await self.db.delete(comment_to_delete)
        await self.db.commit()


def get_comment_service(db: AsyncSession = Depends(get_db)):
    return CommentService(db=db)
