from typing import Union

from fastapi import APIRouter

from src.common.base_schemas import ErrorResponse, SuccessResponse
from src.routes.utils import fetch_vk_user_data, fetch_vk_user_posts
from src.schemas.posts import PostData, UserProfile

router = APIRouter()


async def get_posts_data(method: str, profile: str) -> Union[SuccessResponse, ErrorResponse]:
    if method != 'posts':
        return ErrorResponse(status="error", code=400, message="Unsupported method")

    # Получаем данные профиля
    user_data_response = await fetch_vk_user_data(profile)

    if user_data_response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Invalid account name")

    response_data = user_data_response.json().get("response", [])
    if not response_data:
        return ErrorResponse(status="error", code=403, message="Invalid account name")
    user_data = response_data[0]

    user_id = user_data.get("id")

    # Получаем последние 10 постов пользователя
    user_posts_response = await fetch_vk_user_posts(user_id)

    if user_posts_response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Failed to get posts")

    raw_posts_data = user_posts_response.json().get("response", {}).get("items", [])

    posts_data = []
    for post in raw_posts_data:
        post_details = PostData(
            post_id=f"{user_id}_{post.get('id')}",
            url=f"https://vk.com/wall{user_id}_{post.get('id')}",
            likes=str(post["likes"]["count"]),
            share=str(post["reposts"]["count"]),
            views=str(post["views"]["count"])
        )
        posts_data.append(post_details)

    return SuccessResponse(
        status="success",
        code=200,
        data=UserProfile(
            profile_id=str(user_id),
            avatar_url=user_data.get("photo_max_orig"),
            posts=posts_data
        )
    )
