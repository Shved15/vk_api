from pydantic import BaseModel


class ProfileData(BaseModel):
    profile_id: str
    avatar_url: str
    followers: str
    following: str


# Модель для успешного ответа
class SuccessResponse(BaseModel):
    status: str
    code: int
    data: ProfileData


# Модель для ошибочного ответа
class ErrorResponse(BaseModel):
    status: str
    code: int
    message: str
