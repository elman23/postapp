import pytest
from fastapi import status
from app import schemas
from .database import client, session
import pytest


@pytest.fixture
def test_user(client):
    user_data = {"email": "test@email.com", "password": "password"}
    response = client.post("/users", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    new_user = response.json()
    new_user["password"] = user_data["password"]
    return new_user


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
def test_login_user(client, test_user):
    print("Testing user login...")
    response = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    assert response.status_code == status.HTTP_200_OK
