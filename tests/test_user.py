from fastapi import status
from app import schemas
from .database import client, session


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


# Bad practice: this test depends on test_create_user!
def test_login_user(client):
    print("Testing user login...")
    response = client.post("/login", data={"username": "test@email.com", "password": "password"})
    assert response.status_code == status.HTTP_200_OK
