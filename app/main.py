from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.user import User

app = FastAPI()

# ...


@app.get("/users")
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(User))
    return result.all()


# ...


class Item(BaseModel):
    text: str = ""
    is_done: bool = False


items: list[Item] = []


@app.get("/")
def root() -> dict[str, str]:
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item) -> list[Item]:
    items.append(item)
    return items


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10) -> list[Item]:
    return items[0:limit]


@app.post("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found.")
