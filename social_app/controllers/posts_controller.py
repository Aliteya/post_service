from fastapi import APIRouter, Response, status, HTTPException
from ..schemas import Post
from random import randrange

##ТУТ ПОКА ПРИКИДЫВАЮ РЕАЛИЗАЦИЮ ДУМАЮ НАД БДШКОЙ

post_router = APIRouter(prefix="/posts", tags=["posts"])

posts = [{"title": "title 1", "content": "content1", "id": 1}, {"title": "title 2", "content": "content2", "id": 2}]

def find_by_id(id: int):
    for post in posts:
        if post["id"] == id:
            return post

@post_router.get("/all")
def get_posts():
    return {"data": posts}

@post_router.get("/{id}")
def get_post(id: int, response: Response):
    post = find_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"data": post}

@post_router.post("/createposts",status_code=status.HTTP_201_CREATED)
def create_posts(new_post: Post):
    new_post = new_post.model_dump()
    new_post["id"] = randrange(0, 100000)
    posts.append(new_post)
    return {"data": new_post}

