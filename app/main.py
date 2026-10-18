from fastapi import FastAPI

from app.api.comment import router as comment_router
from app.api.entry import router as entry_router
from app.api.user import router as user_router

app = FastAPI()

app.include_router(entry_router)
app.include_router(user_router)
app.include_router(comment_router)
