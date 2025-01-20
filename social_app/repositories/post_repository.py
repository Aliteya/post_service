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
        return self.session.query()

    def create_post(self, post_schema: PostSchema) -> Post:
        return Post(title=post_schema.title, content=post_schema.content, published=post_schema.published , rating=post_schema.rating)

    def update_all_posts(self):
        pass

    def update_post_by_id(self, id: int) -> Post:
        pass

    def delete_post_by_id(self, id: int) -> bool:
        pass