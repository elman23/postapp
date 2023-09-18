import random
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


post_list = [
    {
        "id": 1,
        "title": "My first post",
        "content": "This is the content",
        "published": False,
        "rating": 3
    },
    {
        "id": 2,
        "title": "My first post",
        "content": "This is the content",
        "published": False,
        "rating": 3
    }
]


@app.get("/posts")
async def get_posts():
    return {"data": post_list}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = random.randint(1, 1000)
    post_list.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = _find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found.")
    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = _find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found.")
    post_list.pop(int(index))
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = _find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found.")
    post_dict = post.dict()
    post_dict["id"] = id
    post_list[index] = post_dict
    return {"data": post_dict}


def _find_index_post(id: int):
    for i, p in enumerate(post_list):
        if p["id"] == id:
            return i
    return None


def _find_post(id: int):
    for p in post_list:
        if p["id"] == id:
            return p
    return None