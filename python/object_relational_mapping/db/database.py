"""This module will contain database connection and necessary methods"""
import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# imports env variables from .env file skips if already env variable assigned
load_dotenv()

database_url=os.getenv('DATABASE_URL')
engine = create_engine(
    database_url
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get a database session
def get_db() -> Session:
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used
    finally:
        db.close()  # Close the session when done