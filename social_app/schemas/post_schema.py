from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostSchema):
    pass

class PostResponse(PostSchema):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True