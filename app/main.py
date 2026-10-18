from datetime import datetime

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.entry import Entry
from app.models.user import User
from app.schemas.entry import EntryCreate, EntryDelete, EntryUpdate
from app.schemas.user import UserCreate

app = FastAPI()


@app.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(User))
    return result.all()


@app.post("/users")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(
        email=user.email, created_at=datetime.now(), updated_at=datetime.now()
    )
    db.add(new_user)
    await db.commit()
    return "Succesfully created a user."


@app.post("/entries")
async def create_entry(entry: EntryCreate, db: AsyncSession = Depends(get_db)):
    new_entry = Entry(
        title=entry.title,
        content=entry.content,
        created_by_id=entry.created_by_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db.add(new_entry)
    await db.commit()
    return "Succesfully created an entry."


@app.get("/entries")
async def read_entries(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(Entry))
    return result.all()


@app.patch("/entry")
async def update_entry(entry: EntryUpdate, db: AsyncSession = Depends(get_db)):
    entry_to_update = await db.get(Entry, entry.id)
    if not entry_to_update:
        return "No entry with the given id found."
    if entry.title:
        entry_to_update.title = entry.title
    if entry.content:
        entry_to_update.content = entry.content

    await db.commit()
    return "Successfully updated given entry."


@app.delete("/entry")
async def delete_entry(entry: EntryDelete, db: AsyncSession = Depends(get_db)):
    entry_to_delete = await db.get(Entry, entry.id)
    if not entry_to_delete:
        return "No entry with the given id found."

    await db.delete(entry_to_delete)
    await db.commit()

    return "Successfuly deleted given entry."
