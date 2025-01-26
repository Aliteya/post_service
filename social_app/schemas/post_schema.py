from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from .user_shema import UserOut

class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostSchema):
    pass

class PostResponse(PostSchema):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    model_config = ConfigDict(from_attributes=True)