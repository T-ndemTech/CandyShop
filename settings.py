from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE URL",
    default="postgresql+asyncpg://postgres:qwert@localhost:5432/CandyShop"
)