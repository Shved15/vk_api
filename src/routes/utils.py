import httpx

from config import (ACCESS_TOKEN, VK_SUBSCRIPTION_URL, VK_USER_GET_ULR,
                    VK_WALL_URL, VK_WALL_URL_GBI)


async def fetch_vk_user_data(profile: str):
    """Получаем данные пользователя по его id или короткому имени"""

    async with httpx.AsyncClient() as client:
        response = await client.get(VK_USER_GET_ULR, params={
            "user_ids": profile,
            "fields": "photo_max_orig,followers_count",
            "v": "5.131",
            "access_token": ACCESS_TOKEN
        })
    return response


async def fetch_vk_subscriptions(user_id: int):
    """Получаем подписки пользователя"""

    async with httpx.AsyncClient() as client:
        response = await client.get(VK_SUBSCRIPTION_URL, params={
            "user_id": user_id,
            "extended": 0,
            "v": "5.131",
            "access_token": ACCESS_TOKEN
        })
    return response


async def fetch_vk_user_posts(user_id: int, count: int = 10):
    """Получаем посты пользователя"""

    async with httpx.AsyncClient() as client:
        response = await client.get(VK_WALL_URL, params={
            "owner_id": user_id,
            "count": count,
            "v": "5.131",
            "access_token": ACCESS_TOKEN
        })
    return response


async def fetch_vk_post_data(post_id: str):
    """Получаем данные поста"""

    async with httpx.AsyncClient() as client:
        response = await client.get(VK_WALL_URL_GBI, params={
            "posts": post_id,
            "v": "5.131",
            "access_token": ACCESS_TOKEN
        })
    return response
