from fastapi import APIRouter

from src.handlers.posts import get_posts_data
from src.handlers.users import get_user

router = APIRouter()


@router.get("/profile-data/")
async def combined_method(method: str, profile: str):
    """Обработчик для получения данных о профиле и постах в одном роутере."""
    return await get_user(method, profile) if method == 'profile' else await get_posts_data(method, profile)
