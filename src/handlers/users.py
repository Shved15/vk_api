from fastapi import APIRouter, FastAPI, HTTPException

from src.common.base_schemas import ErrorResponse, SuccessResponse
from src.routes.utils import fetch_vk_subscriptions, fetch_vk_user_data
from src.schemas.users import ProfileData

router = APIRouter()

api = FastAPI()


async def get_user(method: str, profile: str):
    """Получение данных пользователя"""

    if method != 'profile':
        return ErrorResponse(status="error", code=400, message="Unsupported method")

    # Получение данных пользователя (routes/utils.py)
    user_data_response = await fetch_vk_user_data(profile)

    if user_data_response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Invalid account name")

    response_data = user_data_response.json().get("response", [])
    if not response_data:
        return ErrorResponse(status="error", code=403, message="Invalid account name")
    user_data = response_data[0]

    user_id = user_data.get("id")

    # Получение подписок пользователя (routes/utils.py)
    subscriptions_data_response = await fetch_vk_subscriptions(user_id)

    if subscriptions_data_response.status_code != 200:
        raise HTTPException(status_code=403, detail="Failed to get subscriptions")

    # Общее количество подписок (сообщества + пользователи)
    subscriptions_data = subscriptions_data_response.json().get("response", {})
    total_subscriptions = str(subscriptions_data.get("users", {}).get("count", 0) +
                              subscriptions_data.get("groups", {}).get("count", 0))

    return SuccessResponse(
        status="success",
        code=200,
        data=ProfileData(
            profile_id=str(user_data.get("id")),
            avatar_url=user_data.get("photo_max_orig"),
            followers=str(user_data.get("followers_count")),
            following=total_subscriptions
        )
    )
