from typing import List

from pydantic import BaseModel


class PostData(BaseModel):
    post_id: str
    url: str
    likes: str
    share: str
    views: str


class UserProfile(BaseModel):
    profile_id: str
    avatar_url: str
    posts: List[PostData]
