from fastapi.testclient import TestClient
from social_app import social_app, models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from social_app.models import Base
from social_app.database import get_db
from social_app.auth.oauth2 import create_access_token
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

@pytest.fixture
def test_user(client):
    user_data = {'email': 'alyalu004@gmail.com', 'password': '1234'}
    response = client.post("/users/createusers/", json=user_data)

    assert response.status_code == 201
    new_user = response.json()
    new_user['password'] = user_data['password']
    return new_user

@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})

@pytest.fixture
def authorize_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client

@pytest.fixture
def test_posts(test_user, session):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user['id']
        }, {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user['id']
        }, {
        "title": "3rd title" ,
        "content": "3rd content",
        "owner id": test_user['id'] 
    }]
    def create_post_model(post):
        return models.Post(**post)

    posts = list(map(create_post_model, posts_data))


    session.add_all(posts)
    session.commit()
    posts = session.query(models.Post).all()
    return posts