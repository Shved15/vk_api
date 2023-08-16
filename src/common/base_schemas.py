from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class SuccessResponse(BaseModel, Generic[T]):
    status: str
    code: int
    data: T


class ErrorResponse(BaseModel):
    status: str
    code: int
    message: str
