from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/posts")
async def get_posts():
    return {"data": "This is your post!"}


@app.post("/createpost")
def create_posts(post: Post):
    print(post.model_dump())
    return {"data": post}
