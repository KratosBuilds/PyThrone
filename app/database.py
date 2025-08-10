import aiosqlite
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
import os

# Database URL for SQLite
DATABASE_URL = "sqlite+aiosqlite:///./pythrone.db"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create async session maker
async_session = async_sessionmaker(engine, expire_on_commit=False)

# Create declarative base for models
Base = declarative_base()

# Dependency to get database session
async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

# Create tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)