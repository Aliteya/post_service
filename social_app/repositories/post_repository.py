from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from ..models import Post, Vote
from fastapi import Depends
from ..schemas import PostCreate, PostOut, PostResponse
from typing import List, Optional

class PostRepository():
    def __init__(self, db_session: Session = Depends(get_db)):
        self.session = db_session

    def get_posts(self, limit: int, skip: int, search: Optional[str])-> List[PostOut]:
        posts = self.session.query(Post, func.count(Vote.post_id).label("votes")).join(Vote, Vote.post_id == Post.id, isouter=True).group_by(Post.id).filter(Post.title.contains(search)).limit(limit).offset(skip).all()
        return posts

    def get_post_by_id(self, id: int) -> PostOut:
        post =  self.session.query(Post, func.count(Vote.post_id).label("votes")).join(Vote, Vote.post_id == Post.id, isouter=True).group_by(Post.id).filter(Post.id == id).first()
        return post 

    def create_post(self, **kwargs) -> Post:
        new_post = Post(**kwargs)
        self.session.add(new_post)
        self.session.commit()
        self.session.refresh(new_post)
        return new_post
    
    def update_post_by_id(self, id: int, post_shema: PostCreate) -> Post:
        self.session.query(Post).filter(Post.id == id).update(post_shema.model_dump(), synchronize_session=False)
        self.session.commit()
    
    def delete_post_by_id(self, id: int):
        post = self.session.query(Post).filter(Post.id == id)
        post.delete(synchronize_session=False)
        self.session.commit()