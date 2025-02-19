from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .core import settings
from .models import Base

engine = create_engine(settings.get_url(), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()