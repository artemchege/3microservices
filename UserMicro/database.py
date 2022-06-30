import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from db_creds import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB

# Async setup
ASYNC_SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                          f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL, future=True, echo=True)
async_session_local = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


# Sync setup
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                          f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
sync_engine = create_engine(SQLALCHEMY_DATABASE_URL, )
sync_session_local = sessionmaker(bind=sync_engine, autocommit=False, autoflush=False,)

dsn = f'dbname = {POSTGRES_DB} user = {POSTGRES_USER} password = {POSTGRES_PASSWORD} host = {POSTGRES_HOST}'

Base = declarative_base()


def get_sync_db():
    db = sync_session_local()
    try:
        yield db
    finally:
        db.close()
