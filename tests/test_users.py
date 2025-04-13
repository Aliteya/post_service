from social_app import schemas
from jose import jwt
from social_app.core import jwt_settings
import pytest

def test_root(client):
    response = client.get("/")
    assert response.json().get('data') == 'Hello World'
    assert response.status_code == 200
    
def test_create_users(client):
    response = client.post("/users/createusers/", json={'email': 'alyalu004@gmail.com', 'password': '1234'})
    new_client = schemas.user_shema.UserOut(**response.json())
    assert new_client.email == 'alyalu004@gmail.com'
    assert response.status_code == 201

def test_login_user(client, test_user):
    response = client.post("/auth/login/", data={'username': test_user['email'], 'password': test_user['password']})
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, jwt_settings.SECRET_KEY, algorithms=[jwt_settings.ALGORITHM])
    id: str = payload.get("user_id")
    assert id == test_user['id']
    assert login_response.token_type == "bearer token"
    assert response.status_code == 200


@pytest.mark.parametrize("email, password, status_code", [("wr@gmail.com", "wrong", 403), (None, "pass", 403)])
def test_incorrect_login(test_user, client, email, password, status_code):
    response = client.post("/auth/login/", data={'username': email, 'password': password})
    assert response.status_code == status_code
    # assert response.json().get('detail') == 'invalid credentials'