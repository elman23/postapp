import pytest
from fastapi import status
from app import schemas


def test_get_all_post(authorized_client, test_posts):
    print("Testing get all posts...")
    response = authorized_client.get("/posts/")
    posts = [schemas.ResponsePostVote(**post) for post in response.json()]
    assert posts
    assert len(posts) == len(test_posts)
    assert response.status_code == status.HTTP_200_OK


def test_unauthorized_user_get_all_posts(client, test_posts):
    print("Testing unauthorized client getting all posts...")
    response = client.get("/posts/")
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
    print("Testing authorized client getting existent posts...")
    test_post = test_posts[0]
    response = authorized_client.get(f"/posts/{test_post.id}")
    assert response.status_code == status.HTTP_200_OK
    post = schemas.ResponsePostVote(**response.json())
    assert post.Post.id == test_post.id
    assert post.Post.title == test_post.title
    assert post.Post.content == test_post.content


@pytest.mark.parametrize("title, content, published", [
    ("Awesome title", "Awesome content", False),
    ("Pizzas", "Favourite pizza: pineapple", True),
    ("Skyscrapers", "Tallest skyscraper", False),
    ("Odd", "Odd content", True),
    ("Hi there!", "Hi there!", False),
])
def test_create_post(authorized_client, test_user, title, content, published):
    response = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    assert response.status_code == status.HTTP_201_CREATED
    post = schemas.ResponsePost(**response.json())
    assert post.title == title
    assert post.content == content
    assert post.published == published
    assert post.owner_id == test_user["id"]


def test_create_post_default_published(authorized_client, test_user):
    title = "Test title"
    content = "Test content"
    response = authorized_client.post("/posts/", json={"title": title, "content": content})
    assert response.status_code == status.HTTP_201_CREATED
    post = schemas.ResponsePost(**response.json())
    assert post.title == title
    assert post.content == content
    assert post.published is True
    assert post.owner_id == test_user["id"]


def test_unauthorized_user_create_post(client, test_user):
    print("Testing unauthorized client creating a post...")
    title = "Test title"
    content = "Test content"
    response = client.post("/posts/", json={"title": title, "content": content})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_unauthorized_user_delete_post(client, test_user, test_posts):
    print("Testing unauthorized client deleting a post...")
    response = client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_authorized_user_delete_post(authorized_client, test_user, test_posts):
    response = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_delete_not_existing_post(authorized_client, test_user):
    not_existent_id = 1000
    response = authorized_client.delete(f"/posts/{not_existent_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_other_users_post(authorized_client, test_user, test_other_user, test_posts):
    other_users_post = [post for post in test_posts if post.owner_id == test_other_user["id"]]
    other_users_post_id = other_users_post[0].id
    response = authorized_client.delete(f"/posts/{other_users_post_id}")
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title": "Updated title",
        "content": "Updated content",
        "id": test_posts[0].id
    }
    response = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    assert response.status_code == status.HTTP_200_OK
    updated_post = schemas.ResponsePost(**response.json())
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]


def test_update_other_users_post(authorized_client, test_user, test_other_user, test_posts):
    data = {
        "title": "Updated title",
        "content": "Updated content",
        "id": test_posts[0].id
    }
    other_users_post = [post for post in test_posts if post.owner_id == test_other_user["id"]]
    other_users_post_id = other_users_post[0].id
    response = authorized_client.put(f"/posts/{other_users_post_id}", json=data)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_unauthorized_user_update_post(client, test_user, test_posts):
    print("Testing unauthorized client updating a post...")
    response = client.put(f"/posts/{test_posts[0].id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_update_not_existing_post(authorized_client, test_user, test_posts):
    not_existent_id = 1000
    data = {
        "title": "Updated title",
        "content": "Updated content",
        "id": test_posts[0].id
    }
    response = authorized_client.put(f"/posts/{not_existent_id}", json=data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
