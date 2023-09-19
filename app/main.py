import time
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import random


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


post_list = [
    {
        "id": 1,
        "title": "My first post",
        "content": "This is the first content",
        "published": False,
    },
    {
        "id": 2,
        "title": "My second post",
        "content": "This is the second content",
        "published": False,
    }
]


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="root",
            password="root",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection successful.")
        break
    except Exception as error:
        print("Connecting to database failed!")
        print("Error:", error)
        time.sleep(1)


@app.get("/")
async def get_posts():
    return {"message": "Hello, World!"}


@app.get("/posts")
async def get_posts():
    cursor.execute(
        """select * from posts"""
    )
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute(
        """insert into posts (title, content, published) values (%s, %s, %s) returning *""",
        (post.title, post.content, post.published)
    )
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute(
        """select * from posts where id = %s""",
        (str(id),)
    )
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found.")
    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute(
        """delete from posts where id = %s returning *""",
        (str(id),)
    )
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found.")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute(
        """update posts set title = %s, content = %s, published = %s where id = %s returning *""",
        (post.title, post.content, post.published, str(id))
    )
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} was not found.")
    return {"data": updated_post}