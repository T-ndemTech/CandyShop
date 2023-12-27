from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
import settings

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:qwert@localhost:5432/CandyShop"

engine = create_async_engine(settings.REAL_DATABASE_URL)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()