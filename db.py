from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Query
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
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = 5432


# Connecting DataBase
db_engine = create_engine(
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}",echo=True)

# Session Object for making transactions
Session = sessionmaker(bind=db_engine)