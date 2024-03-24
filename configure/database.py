
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from configure.config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    #pool_size=5,
    #max_overflow=10
)
session = async_sessionmaker(engine, )

class Base(DeclarativeBase):
    pass