from jose import jwt
from fastapi import status
from app import schemas
from app.config import settings


def test_root(client):
    print("Testing root path of application...")
    response = client.get("/")
    assert response.json().get("message") == "Post API"
    assert response.status_code == status.HTTP_200_OK


def test_create_user(client):
    print("Testing user creation...")
    response = client.post("/users", json={"email": "test@email.com", "password": "password"})
    new_user = schemas.ResponseUser(**response.json())
    assert new_user.email == "test@email.com"
    assert response.status_code == status.HTTP_201_CREATED


def test_login_user(client, test_user):
    print("Testing user login...")
    response = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    assert response.status_code == status.HTTP_200_OK
    login_response = schemas.Token(**response.json())
    payload = jwt.decode(login_response.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user["id"]
    assert login_response.token_type == "bearer"


def test_incorrect_login(client, test_user):
    print("Testing incorrect user login...")
    response = client.post("/login", data={"username": test_user["email"], "password": "wrong"})
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json().get("detail") == "Invalid credentials"
