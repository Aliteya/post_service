from .base import Base
from datetime import datetime
from sqlalchemy.sql.expression import text
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    published: Mapped[bool] = mapped_column(server_default='TRUE', nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=text('NOW()'))

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")