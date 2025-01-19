from fastapi import FastAPI
from utils import create_table, add_book, delete_book, get_all_books

app = FastAPI()


@app.get("/")
def read_root():
    return {"The": "Library"}
