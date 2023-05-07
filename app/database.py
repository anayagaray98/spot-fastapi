from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv
from app.environment import ENVIRONMENT
from dotenv import load_dotenv

if ENVIRONMENT=='PROD':
    load_dotenv('prod.env')
else:
    load_dotenv('.env')
#______________________________________________________________
POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_PORT = getenv("POSTGRES_PORT")
POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_HOSTNAME = getenv("POSTGRES_HOSTNAME")
#______________________________________________________________
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()