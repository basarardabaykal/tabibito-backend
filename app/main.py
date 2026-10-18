from fastapi import FastAPI

from app.api.entry import router as entry_router
from app.api.user import router as user_router

app = FastAPI()

app.include_router(entry_router)
app.include_router(user_router)
