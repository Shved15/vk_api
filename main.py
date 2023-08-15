from fastapi import FastAPI

from src.routes.users import router as user_router
from src.routes.likes import router as like_router
from src.routes.posts import router as post_router

app = FastAPI()

prefix = '/api/v1'

app.include_router(user_router, prefix=prefix)
app.include_router(like_router, prefix=prefix)
app.include_router(post_router, prefix=prefix)
