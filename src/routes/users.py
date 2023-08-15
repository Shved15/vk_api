from fastapi import FastAPI, HTTPException, APIRouter
import requests

from config import ACCESS_TOKEN, VK_USER_GET_ULR, VK_SUBSCRIPTION_URL
from src.schemas.users import ErrorResponse, SuccessResponse, ProfileData

router = APIRouter()

api = FastAPI()


@router.get("/profile/")
async def get_user(method: str, profile: str):
    if method != 'profile':
        return ErrorResponse(status="error", code=400, message="Unsupported method")

    response = requests.get(VK_USER_GET_ULR, params={
        "user_ids": profile,
        "fields": "photo_max_orig,followers_count",
        "v": "5.131",
        "access_token": ACCESS_TOKEN
    })

    if response.status_code != 200:
        raise HTTPException(status_code=403, detail="Invalid account name")

    user_data = response.json().get("response", [{}])[0]
    user_id = user_data.get("id")

    # Получение подписок
    subscriptions_response = requests.get(VK_SUBSCRIPTION_URL, params={
        "user_id": user_id,
        "extended": 0,
        "v": "5.131",
        "access_token": ACCESS_TOKEN
    })

    if subscriptions_response.status_code != 200:
        raise HTTPException(status_code=403, detail="Failed to get subscriptions")

    subscriptions_data = subscriptions_response.json().get("response", {})
    print(subscriptions_response.json())
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
