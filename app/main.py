from fastapi import FastAPI
from . import auth
from .routers import post, user, vote
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine


# Auto generate database
# models.Base.metadata.create_all(bind=engine)
app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Post API"}
