from pydantic import BaseModel
from typing import Optional

class PostSchema(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None