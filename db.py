from sqlalchemy.ext.asyncio import create_async_engine
# Settings Module
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# DB_PARAMETERS FROM .env
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USERNAME = os.getenv("USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = 5432


# Async Connecting DataBase
db_engine = create_async_engine(
    f"postgresql+asyncpg://user:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")


