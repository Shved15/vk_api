from fastapi import FastAPI

from src.middlewares.api_middleware import SingleRequestMiddleware
from src.routes.likes import router as like_router
from src.routes.profile import router as profile_router

app = FastAPI()

prefix = '/api/v1'

app.add_middleware(SingleRequestMiddleware)
app.include_router(like_router, prefix=prefix)
app.include_router(profile_router, prefix=prefix)
