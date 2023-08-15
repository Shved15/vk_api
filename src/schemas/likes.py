
from pydantic import BaseModel


class PostData(BaseModel):
    post_id: str
    url: str
    likes: str
    share: str
    views: str


class SuccessResponse(BaseModel):
    status: str
    code: int
    data: PostData


class ErrorResponse(BaseModel):
    status: str
    code: int
    message: str
