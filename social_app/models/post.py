from .base import Base
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    pudlished: Mapped[bool] = mapped_column(default=True)
    rating: Mapped[int] = mapped_column()
    created_at: Mapped[datetime] = mapped_column()