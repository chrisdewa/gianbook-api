from sqlalchemy import (
    Boolean,
    Column, 
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from .config import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    posts = relationship('Post', back_populates='author')


class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='posts')
    
    