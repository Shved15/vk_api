from fastapi import APIRouter

from src.handlers.posts import get_posts_data
from src.handlers.users import get_user

router = APIRouter()


@router.get("/api/v1/profile-data/")
async def combined_method(method: str, profile: str):
    return await get_user(method, profile) if method == 'profile' else await get_posts_data(method, profile)
