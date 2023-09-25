from fastapi.testclient import TestClient
from fastapi import status
from app.main import app
from app import schemas
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import get_db, Base


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine) # Generate database tables


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_root():
    response = client.get("/")
    print("Testing root path of application.")
    assert response.json().get("message") == "Post API"
    assert response.status_code == status.HTTP_200_OK


def test_create_user():
    response = client.post("/users", json={"email": "test@email.com", "password": "password"})
    new_user = schemas.ResponseUser(**response.json())
    assert new_user.email == "test@email.com"
    assert response.status_code == status.HTTP_201_CREATED
