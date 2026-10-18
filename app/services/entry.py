from datetime import datetime

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.results import DetailedResult
from app.db.session import get_db
from app.models.entry import Entry
from app.schemas.entry import EntryCreate, EntryDelete, EntryUpdate


class EntryService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_entry(self, entry_in: EntryCreate):
        new_entry = Entry(
            title=entry_in.title,
            content=entry_in.content,
            created_by_id=entry_in.created_by_id,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        self.db.add(new_entry)
        await self.db.commit()

    async def read_entries(self):
        entries = await self.db.scalars(select(Entry))

        return DetailedResult[list[Entry]](
            is_successful=True,
            message="Successfully retrieved all entries.",
            data=list(entries.all()),
        )

    async def update_entry(self, entry_in: EntryUpdate):
        entry_to_update = await self.db.get(Entry, entry_in.id)
        if not entry_to_update:
            return DetailedResult[None](False, "No entry with the given id found.")

        update_data = entry_in.model_dump(exclude_defaults=True)
        for key, value in update_data.items():
            setattr(entry_to_update, key, value)

        await self.db.commit()

    async def delete_entry(self, entry_in: EntryDelete):
        entry_to_delete = await self.db.get(Entry, entry_in.id)
        if not entry_to_delete:
            return DetailedResult[None](False, "No entry with the given id found.")

        await self.db.delete(entry_to_delete)
        await self.db.commit()


def get_entry_service(db: AsyncSession = Depends(get_db)) -> EntryService:
    return EntryService(db=db)
