from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    print("Testing root path of application.")
    assert response.json().get("message") == "Post API"
    assert response.status_code == 200
