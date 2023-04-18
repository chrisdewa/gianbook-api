from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.db import models, schemas

async def get_user(db: AsyncSession, user_id: int):
    stmt = select(models.User).where(models.User.id == user_id)
    return await db.execute(stmt)


async def get_user_by_username(db: AsyncSession, username: str):
    stmt = select(models.User).where(models.User.username == username).limit(1)
    return await db.execute(stmt)

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(models.User).offset(skip).limit(limit)
    return await db.execute(stmt)

async def create_user(db: AsyncSession, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_posts(db: AsyncSession, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


async def create_user_post(db: AsyncSession, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item