from fastapi import status


def test_get_all_post(authorized_client, test_posts):
    print("Testing get all posts...")
    response = authorized_client.get("/posts")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
