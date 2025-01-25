from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Post
from fastapi import Depends
from ..schemas import PostCreate
from typing import List, Optional

class PostRepository():
    def __init__(self, db_session: Session = Depends(get_db)):
        self.session = db_session

    def get_posts(self, limit: int, search: Optional[str]) -> List[PostCreate]:
        return self.session.query(Post).filter(Post.title.contains(search)).limit(limit).all()

    def get_post_by_id(self, id: int) -> Post:
        return self.session.query(Post).filter(Post.id == id).first()

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