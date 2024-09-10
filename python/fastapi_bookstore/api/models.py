""""This module contains api models for fastapi"""
from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    """book request class"""
    id: str = Field(..., description= "Book unique id", example= "id1001")
    title: str = Field(...,
                       description= "Book title",
                       example= "To Kill a Mockingbird")
    author: str = Field(...,
                        description= "author name",
                        example= "Harper Lee")
    isbn: str |None
    published_date: date | None

class BookResponse(BaseModel):
    """book response class"""
    title: str = Field(...,
                       description= "Book title",
                       example= "To Kill a Mockingbird")
    author: str = Field(...,
                        description= "author name",
                        example= "Harper Lee")
    isbn: str |None
    published_date: date | None
