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
def create_posts(new_post: PostSchema, db: Session = Depends(get_db)):
    post_repo = PostRepository(db)
    new_post = post_repo.create_post(new_post)
    return {"data": new_post}

@post_router.put("updatepost")
def update_post(id: int, post: PostSchema, db: Session = Depends(get_db)):
    post_repo = PostRepository(db)
    search_post = post_repo.get_post_by_id(id)
    if search_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
    post_repo.update_post_by_id(id, post)
    return {"data": search_post}

@post_router.delete("deletepost", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post_repo = PostRepository(db)
    deleted_post = post_repo.get_post_by_id(id)
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
    post_repo.delete_post_by_id(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
