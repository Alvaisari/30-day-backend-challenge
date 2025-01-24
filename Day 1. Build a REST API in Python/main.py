import sqlite3
from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from utils import create_table, add_book, delete_book, get_all_books


class Book(BaseModel):
    """Pydantic model for requests"""

    name: str
    author: str


def lifespan(app: FastAPI):
    """Lifespan function to handle startup and shutdown"""
    print("Starting up the up")
    # Create table with books if it doesn't exist yet
    create_table()
    yield
    print("Shutting down")


app = FastAPI(lifespan=lifespan)


# FastAPI endpoints
@app.get("/")
def read_root():
    return {"The": "Library"}


@app.post("/books/", response_model=Book, status_code=201)
async def create_book(book: Book):
    """Adds a book to the database"""
    try:
        add_book(book.name, book.author)
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=401, detail="The book already exists!") from e
    except Exception as e:
        raise HTTPException(
            status_code=501, detail=f"Error adding the book: {e}"
        ) from e
    return book


@app.get("/books", response_model=List[Book])
async def get_books():
    """Get the list of all books in the database"""
    list_of_books = get_all_books()
    return [{"name": name, "author": author} for name, author in list_of_books]


@app.delete("/books/{book_name}")
async def remove_book_by_name(book_name: str):
    """Removes a book from the database by its name"""
    try:
        delete_book(book_name)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e)) from e
    return {"message": f"The book {book_name} was deleted."}
