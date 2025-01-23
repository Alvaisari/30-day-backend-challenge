from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from utils import create_table, add_book, delete_book, get_all_books


class Book(BaseModel):
    """Pydantic model for requests"""

    name: str
    author: str


create_table()
app = FastAPI()


# FastAPI endpoints
@app.get("/")
def read_root():
    return {"The": "Library"}


@app.post("/books", response_model=Book, status_code=201)
async def create_book(book: Book):
    """Adds a book to the database"""
    try:
        add_book(book.name, book.author)
    except Exception as e:
        raise HTTPException(status_code=501, detail=str(e)) from e
    return {"message": "The book was created successfully!"}


@app.get("/books", response_model=List[Book])
async def get_books():
    """Get the list of all books in the database"""
    return get_all_books()


@app.delete("/books/{book_name}")
async def remove_book_by_name(book_name: str):
    """Removes a book from the database by its name"""
    try:
        delete_book(book_name)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e)) from e
    return {"message": f"The book {book_name} was deleted."}
