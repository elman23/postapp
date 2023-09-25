from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base
import pytest
from alembic import command


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    # Run code before test run
    Base.metadata.drop_all(bind=engine)  # Drop database tables
    Base.metadata.create_all(bind=engine)  # Generate database tables
    # command.upgrade(head) # Alembic version
    # Yield client
    yield TestClient(app)
    # Run code after test finishes
    # Base.metadata.drop_all(bind=engine)  # Drop database tables
    # command.downgrade(base)


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
