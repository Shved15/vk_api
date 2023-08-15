# schemas/response.py
from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar('T')


class SuccessResponse(BaseModel, Generic[T]):
    status: str
    code: int
    data: T


class ErrorResponse(BaseModel):
    status: str
    code: int
    message: str
