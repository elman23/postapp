from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


### Incoming schemas ###

class BasePost(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(BasePost):
    pass


class UpdatePost(BasePost):
    pass


class BaseUser(BaseModel):
    email: EmailStr
    password: str


class CreateUser(BaseUser):
    pass


### Outgoing schemas ###

class ResponsePost(BasePost):
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        orm_mode = True


class ResponseUser(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


### Token Schema ###

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]
