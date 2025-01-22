from fastapi import APIRouter, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserCreate, UserOut
from ..repositories import UserRepository
from typing import List
from ..utils import hash

user_router = APIRouter(prefix="/users", tags=["users"])

def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

# @user_router.get("/all", response_model=List[PostResponse])
# def get_posts(user_repo: UserRepository = Depends(get_user_repo)):
#     return user_repo.get_all_posts()

@user_router.get("/{id}", response_model=UserOut)
def get_post(id: int, user_repo: UserRepository = Depends(get_user_repo)):
    user = user_repo.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

@user_router.post("/createusers", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_users(new_user: UserCreate, user_repo: UserRepository = Depends(get_user_repo)):
    new_user.password = hash(new_user.password)
    new_user = user_repo.create_user(new_user)
    return new_user

# @user_router.put("/updatepost/{id}", response_model=PostResponse)
# def update_post(id: int, post: PostCreate, user_repo: UserRepository = Depends(get_user_repo)):
#     search_post = user_repo.get_post_by_id(id)
#     if search_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
#     user_repo.update_post_by_id(id, post)
#     return search_post

# @user_router.delete("/deletepost/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, user_repo: UserRepository = Depends(get_user_repo)):
#     deleted_post = user_repo.get_post_by_id(id)
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} not found")
#     user_repo.delete_post_by_id(id)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
