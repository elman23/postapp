from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/posts")
async def get_posts():
    return {"data": "This is your post!"}


@app.post("/createpost")
def create_posts(post: Post):
    print(post)
    return {"data": "new post"}
