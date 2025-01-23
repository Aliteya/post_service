from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import PostCreate, PostResponse
from ..repositories import PostRepository
from ..auth import get_current_user
from typing import List

post_router = APIRouter(prefix="/posts", tags=["posts"])

def get_post_repo(db: Session = Depends(get_db)) -> PostRepository:
    return PostRepository(db)

@post_router.get("/all", response_model=List[PostResponse])
def get_posts(post_repo: PostRepository = Depends(get_post_repo)):
    return post_repo.get_all_posts()

@post_router.get("/{id}", response_model=PostResponse)
def get_post(id: int, post_repo: PostRepository = Depends(get_post_repo)):
    post = post_repo.get_post_by_id(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post

@post_router.post("/createposts",status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_posts(new_post: PostCreate, post_repo: PostRepository = Depends(get_post_repo), user_id: int = Depends(get_current_user)):
    new_post = post_repo.create_post(new_post)
    return new_post

@post_router.put("/updatepost/{id}", response_model=PostResponse)
def update_post(id: int, post: PostCreate, post_repo: PostRepository = Depends(get_post_repo)):
    search_post = post_repo.get_post_by_id(id)
    if search_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
    post_repo.update_post_by_id(id, post)
    return search_post

@post_router.delete("/deletepost/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, post_repo: PostRepository = Depends(get_post_repo)):
    deleted_post = post_repo.get_post_by_id(id)
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
    post_repo.delete_post_by_id(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
