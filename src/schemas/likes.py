
from pydantic import BaseModel


class PostData(BaseModel):
    post_id: str
    url: str
    likes: str
    share: str
    views: str
