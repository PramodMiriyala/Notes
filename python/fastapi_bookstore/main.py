"""this is the main module"""
from fastapi import FastAPI
from datetime import date
from api.models import BookRequest, BookResponse


app = FastAPI()

@app.get("/books", response_model= list[BookResponse])
def get_books():
    """function for getting books"""
    responses = []
    responses.append(BookResponse(
        id = "id1001",
        title = "To Kill a Mockingbird",
        author = "Harper Lee",
        isbn = "978-92-95055-02-5",
        published_date = date.today()
    ))
    return responses

@app.post("/books", response_model= BookResponse)
def create_book(request: BookRequest):
    """create book"""
    response = BookResponse(
        id = request.id,
        title= request.title,
        author= request.author,
        isbn=request.isbn,
        published_date= request.published_date
    )
    return response
