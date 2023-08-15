from fastapi import APIRouter
from typing import Union
import requests

from config import VK_WALL_URL_GBI, ACCESS_TOKEN
from src.schemas.likes import ErrorResponse, SuccessResponse, PostData

router = APIRouter()


@router.get("/likes/", response_model=Union[SuccessResponse, ErrorResponse])
async def get_post_data(method: str, link: str) -> Union[SuccessResponse, ErrorResponse]:
    if method != 'likes':
        return ErrorResponse(status="error", code=400, message="Unsupported method")

    post_id = link.split('wall')[-1]

    response = requests.get(VK_WALL_URL_GBI, params={
        "posts": post_id,
        "v": "5.131",
        "access_token": ACCESS_TOKEN
    })

    if response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Invalid account name")

    post_data = response.json().get("response", [{}])[0]

    if not post_data:
        return ErrorResponse(status="error", code=403, message="Invalid account name")

    # Извлечение необходимых данных
    likes = str(post_data["likes"]["count"])
    shares = str(post_data["reposts"]["count"])
    views = str(post_data["views"]["count"])

    return SuccessResponse(
        status="success",
        code=200,
        data=PostData(
            post_id=post_id,
            url=link,
            likes=likes,
            share=shares,
            views=views
        )
    )
