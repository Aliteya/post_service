from social_app import schemas
from .database import session, client

def test_root(client):
    response = client.get("/")
    assert response.json().get('data') == 'Hello World'
    assert response.status_code == 200
    
def test_create_users(client):
    response = client.post("/users/createusers/", json={'email': 'alyalu004@gmail.com', 'password': '1234'})
    new_client = schemas.user_shema.UserOut(**response.json())
    assert new_client.email == 'alyalu004@gmail.com'
    assert response.status_code == 201
