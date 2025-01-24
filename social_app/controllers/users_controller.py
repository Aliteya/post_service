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