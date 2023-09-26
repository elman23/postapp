import pytest
from fastapi import status
from app import models


@pytest.fixture
def test_vote(session, test_user, test_posts):
    new_vote = models.Vote(post_id=test_posts[3].id, user_id=test_user["id"])
    session.add(new_vote)
    session.commit()


def test_vote_on_post(authorized_client, test_posts):
    response = authorized_client.post("/vote", json={"post_id": test_posts[0].id, "direction": 1})
    assert response.status_code == status.HTTP_201_CREATED


def test_vote_twice_post(authorized_client, test_posts, test_vote):
    response = authorized_client.post("/vote", json={"post_id": test_posts[3].id, "direction": 1})
    assert response.status_code == status.HTTP_409_CONFLICT


def test_vote_delete_post(authorized_client, test_posts, test_vote):
    response = authorized_client.post("/vote", json={"post_id": test_posts[3].id, "direction": 0})
    assert response.status_code == status.HTTP_201_CREATED


def test_vote_down_post(authorized_client, test_posts):
    response = authorized_client.post("/vote", json={"post_id": test_posts[0].id, "direction": 0})
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_vote_not_existent_post(authorized_client, test_posts):
    not_existent_id = 1000
    response = authorized_client.post("/vote", json={"post_id": not_existent_id, "direction": 1})
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_vote_unauthorized_user(client, test_posts):
    response = client.post("/vote", json={"post_id": test_posts[0].id, "direction": 1})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
