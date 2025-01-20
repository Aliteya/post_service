from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Post
from fastapi import Depends
from ..schemas import PostSchema

class PostRepository():
    def __init__(self, db_session: Session = Depends(get_db)):
        self.session = db_session

    def get_all_posts(self) -> list:
        return self.session.query(Post).all()

    def get_post_by_id(self, id: int) -> Post:
        return self.session.query(Post).filter(Post.id == id).first()

    def create_post(self, post_schema: PostSchema) -> Post:
        new_post = Post(post_schema.model_dump())
        self.session.add()
        self.session.commit()
        self.session.refresh()
        return new_post
    
    def update_post_by_id(self, id: int, post_shema: PostSchema) -> Post:
        self.session.query(Post).filter(Post.id == id).update(post_shema.model_dump(), synchronize_session=False)
        self.session.commit()
    
    def delete_post_by_id(self, id: int):
        post = self.session.query(Post).filter(Post.id == id)
        post.delete(synchronize_session=False)
        self.session.commit()