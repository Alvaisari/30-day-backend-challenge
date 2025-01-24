import sqlite3 as sql
from contextlib import contextmanager


@contextmanager
def connect_to_db():
    """Safely open database"""
    try:
        conn = sql.connect("books.db")
        yield conn
    except Exception as e:
        print(f"Can't connect to the database: {e}")
        conn.rollback()
        raise Exception from e
    finally:
        conn.close()


def create_table():
    """Creates table with books"""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE
            IF NOT EXISTS books
            (name TEXT, author TEXT, UNIQUE(name, author))"""
        )
        conn.commit()


def add_book(name, author):
    """Adds a new book to the database"""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO books (name, author)
            VALUES (?, ?)""",
            (name, author),
        )
        conn.commit()


def get_all_books():
    """Get all books from the database"""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM books""")
        list_of_books = cursor.fetchall()
    return list_of_books


def delete_book(name):
    """Delete a book from the database based on its name"""
    with connect_to_db() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """DELETE FROM books
                       WHERE name=?""",
            (name,),
        )
