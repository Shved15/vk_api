from fastapi import APIRouter
from typing import Union
import requests

from config import ACCESS_TOKEN, VK_USER_GET_ULR, VK_WALL_URL
from src.schemas.posts import SuccessResponse, ErrorResponse, PostData, UserProfile

router = APIRouter()


@router.get("/posts/", response_model=Union[SuccessResponse, ErrorResponse])
async def get_posts_data(method: str, profile: str) -> Union[SuccessResponse, ErrorResponse]:
    if method != 'posts':
        return ErrorResponse(status="error", code=400, message="Unsupported method")

    # Получаем данные профиля
    response = requests.get(VK_USER_GET_ULR, params={
        "user_ids": profile,
        "fields": "photo_max_orig",
        "v": "5.131",
        "access_token": ACCESS_TOKEN
    })

    if response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Invalid account name")

    user_data = response.json().get("response", [{}])[0]
    user_id = user_data.get("id")

    # Получаем последние 10 постов пользователя
    posts_response = requests.get(VK_WALL_URL, params={
        "owner_id": user_id,
        "count": 10,
        "v": "5.131",
        "access_token": ACCESS_TOKEN
    })

    if posts_response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Failed to get posts")

    raw_posts_data = posts_response.json().get("response", {}).get("items", [])

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
