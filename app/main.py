from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.comment import router as comment_router
from app.api.entry import router as entry_router
from app.api.user import router as user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entry_router)
app.include_router(user_router)
app.include_router(comment_router)
