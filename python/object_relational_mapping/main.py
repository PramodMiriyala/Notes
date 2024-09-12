"""this is the main module"""
from fastapi import FastAPI, Depends
from datetime import date
from sqlalchemy.orm import Session
from api.schemas import BookRequest, BookResponse
from db.database import SessionLocal,engine,get_db,Base
from db.models import Books

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/books", response_model=list[BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    """This method gets all the books 
    """
    return db.query(Books).all()

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Retrieve a single book by ID."""
    book = db.query(Books).filter(Books.id == book_id).first()  # Query for the book by ID
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")  # Raise 404 if not found
    return book  # Return the book, which will be validated against BookResponse

@app.post("/books", response_model= BookResponse)
def create_book(request: BookRequest, db: Session = Depends(get_db)):
    """create book"""
    db_book = Books(**request.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    book = db.query(Books).filter(Books.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)  # Delete the book from the database
    db.commit()  # Commit the changes to the database
    return {"detail": "Book deleted successfully"}
