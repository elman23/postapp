from fastapi import status
from app import schemas


def test_get_all_post(authorized_client, test_posts):
    print("Testing get all posts...")
    response = authorized_client.get("/posts")
    posts = [schemas.ResponsePostVote(**post) for post in response.json()]
    assert posts
    assert len(posts) == len(test_posts)
    assert response.status_code == status.HTTP_200_OK
