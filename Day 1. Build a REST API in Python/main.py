from fastapi import FastAPI
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


@app.post("/books")
async def create_book(book: Book):
    add_book(book.name, book.author)
    return {"message": "The book was created successfully!"}


@app.get("/books")
async def get_books():
    return get_all_books()


@app.delete("/books/{book_name}")
async def remove_book_by_name(book_name: str):
    delete_book(book_name)
    return {"message": f"The book {book_name} was deleted."}
