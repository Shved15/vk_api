from pydantic import BaseModel


class SuccessResponse(BaseModel):
    status: str
    code: int
    data: BaseModel


class ErrorResponse(BaseModel):
    status: str
    code: int
    message: str
