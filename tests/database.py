from fastapi.testclient import TestClient
from social_app import social_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from social_app.models import Base
from social_app.database import get_db
import pytest

TEST_DATABASE_URL = f"postgresql://postgres:postgres@localhost:5432/social_app_test"

test_engine = create_engine(TEST_DATABASE_URL, echo=True)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    social_app.dependency_overrides[get_db] = override_get_db
    # Base.metadata.create_all(bind=test_engine)
    # command.upgrade("head")
    # Base.metadata.drop_all(bind=test_engine)
    # command.downgrade("base")
    yield TestClient(social_app)
    