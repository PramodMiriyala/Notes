"""This module contains database models"""
from db.database import Base
from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key = True)
    title = Column(String, unique=True, index=True)
    author = Column(String)
    isbn = Column(String)
    published_date = Column(Date)
    