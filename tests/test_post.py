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


def test_unauthorized_user_get_one_post(client, test_posts):
    print("Testing unauthorized client getting one posts...")
    response = client.get(f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authorized_get_not_existent_post(authorized_client, test_posts):
    print("Testing authorized client getting not existent posts...")
    not_existent_id = 1000
    response = authorized_client.get(f"/posts/{not_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_authorized_get_one_post(authorized_client, test_posts):
    print("Testing authorized client getting not existent posts...")
    test_post = test_posts[0]
    response = authorized_client.get(f"/posts/{test_post.id}")
    assert response.status_code == status.HTTP_200_OK
    post = schemas.ResponsePostVote(**response.json())
    assert post.Post.id == test_post.id
    assert post.Post.content == test_post.content

