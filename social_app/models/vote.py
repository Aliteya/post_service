from .base import Base
from sqlalchemy.sql.expression import text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship


class Vote(Base):
    __tablename__ = "votes"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)