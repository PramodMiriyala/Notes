""""This module contains api models for fastapi"""
from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel, Field

class BookRequest(BaseModel):
    """book request class"""
    id: int = Field(..., description= "Book unique id", example= 1001)
    title: str = Field(...,
                       description= "Book title",
                       example= "To Kill a Mockingbird")
    author: str = Field(...,
                        description= "author name",
                        example= "Harper Lee")
    isbn: str |None
    published_date: date | None

    class Config:
        orm_mode = True

class BookResponse(BaseModel):
    """book response class"""
    id: int = Field(..., description= "Book unique id", example= 1001)
    title: str = Field(...,
                       description= "Book title",
                       example= "To Kill a Mockingbird")
    author: str = Field(...,
                        description= "author name",
                        example= "Harper Lee")
    isbn: str |None
    published_date: date | None
    class Config:
        orm_mode = True