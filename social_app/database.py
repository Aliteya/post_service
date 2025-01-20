from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .core import Settings
from .models import Base

settings = Settings()

engine = create_engine(settings.get_url(), echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()