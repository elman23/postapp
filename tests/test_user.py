from fastapi import status
from app import schemas
from .database import client, session


def test_root(client):
    response = client.get("/")
    print("Testing root path of application.")
    assert response.json().get("message") == "Post API"
    assert response.status_code == status.HTTP_200_OK


def test_create_user(client):
    response = client.post("/users", json={"email": "test@email.com", "password": "password"})
    new_user = schemas.ResponseUser(**response.json())
    assert new_user.email == "test@email.com"
    assert response.status_code == status.HTTP_201_CREATED
