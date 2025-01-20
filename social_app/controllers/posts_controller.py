from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PostSchema
from random import randrange
from ..repositories import PostRepository
##ТУТ ПОКА ПРИКИДЫВАЮ РЕАЛИЗАЦИЮ ДУМАЮ НАД БДШКОЙ

post_router = APIRouter(prefix="/posts", tags=["posts"])


post_repo = PostRepository()

@post_router.get("/all")
def get_posts(db: Session = Depends(get_db)):
    post_repo = PostRepository(db)
    return {"data": post_repo.get_all_posts()}

@post_router.get("/{id}")
def get_post(id: int, response: Response):
    post = "f"
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"data": post}

@post_router.post("/createposts",status_code=status.HTTP_201_CREATED)
def create_posts(new_post: PostSchema):
    new_post = new_post.model_dump()
    new_post["id"] = randrange(0, 100000)
    posts.append(new_post)
    return {"data": new_post}

@post_router.put("updateposts")
def update_posts():
    pass

@post_router.patch("updatepost")
def update_post():
    pass

@post_router.delete("deletepost")
def delete_post():
    pass
