from typing import List, Union
from pydantic import BaseModel

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode=True

class User(BaseModel):
    name: str
    email: str
    password: str

class Showuser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: Showuser
    class Config():
        orm_mode=True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None