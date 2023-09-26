from fastapi import status
from app import schemas


def test_get_all_post(authorized_client, test_posts):
    print("Testing get all posts...")
    response = authorized_client.get("/posts")
    posts = [schemas.ResponsePostVote(**post) for post in response.json()]
    assert posts
    assert len(posts) == len(test_posts)
    assert response.status_code == status.HTTP_200_OK


def test_unauthorized_user_get_all_posts(client, test_posts):
    print("Testing unauthorized client getting all posts...")
    response = client.get("/posts")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
