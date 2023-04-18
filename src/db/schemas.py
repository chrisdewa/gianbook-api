from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    description: str

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id: int
    author_id: int
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    posts: list[Post] = []
    
    class Config:
        orm_mode = True
