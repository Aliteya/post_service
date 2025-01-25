from pydantic import BaseModel, Field
from typing_extensions import Annotated

class VoteSchema(BaseModel):
    post_id: int
    dir: Annotated[int, Field(le=1)]