from typing import Union

from fastapi import APIRouter

from src.common.base_schemas import ErrorResponse, SuccessResponse
from src.routes.utils import fetch_vk_post_data
from src.schemas.likes import PostData

router = APIRouter()


@router.get("/likes/", response_model=Union[SuccessResponse, ErrorResponse])
async def get_post_data(link: str, method: str = 'likes') -> Union[SuccessResponse, ErrorResponse]:
    """Получаем актуальные данные поста"""
    if method != 'likes':
        return ErrorResponse(status="error", code=400, message="Unsupported method")

    # Забираем id поста из ссылки
    post_id = link.split('wall')[-1]

    # Получаем данные поста (.utils.py)
    post_data_response = await fetch_vk_post_data(post_id)

    if post_data_response.status_code != 200:
        return ErrorResponse(status="error", code=403, message="Invalid account name")

    post_data = post_data_response.json().get("response", [{}])[0]

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
