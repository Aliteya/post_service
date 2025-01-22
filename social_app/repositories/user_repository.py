from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from fastapi import Depends
from ..schemas import UserCreate

class UserRepository():
    def __init__(self, db_session: Session = Depends(get_db)):
        self.session = db_session

    # def get_all_posts(self) -> list:
    #     return self.session.query(Post).all()

    def get_user_by_id(self, id: int) -> User:
        return self.session.query(User).filter(User.id == id).first()

    def create_user(self, user_schema: UserCreate) -> User:
        new_user = User(**user_schema.model_dump())
        self.session.add(new_user)
        self.session.commit()
        self.session.refresh(new_user)
        return new_user
    
    # def update_post_by_id(self, id: int, post_shema: PostCreate) -> Post:
    #     self.session.query(Post).filter(Post.id == id).update(post_shema.model_dump(), synchronize_session=False)
    #     self.session.commit()
    
    # def delete_post_by_id(self, id: int):
    #     post = self.session.query(Post).filter(Post.id == id)
    #     post.delete(synchronize_session=False)
    #     self.session.commit()