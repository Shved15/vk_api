from pydantic import BaseModel


class ProfileData(BaseModel):
    profile_id: str
    avatar_url: str
    followers: str
    following: str
