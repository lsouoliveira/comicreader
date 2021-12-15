from app import models
from app.exceptions import ResourceNotFound
from app.main.repository.book_repository import save, save_batch, find, find_by_id
from app.models import Book

def save_book(book: Book):
    return save(book)

def get_all_books():
    return find()

def get_book_by_id(id: int):
    book = find_by_id(id)

    if not book:
        raise ResourceNotFound(id)

    return book

def bookmark(id: int, page: int):
    book = get_book_by_id(id)

    book.reading_progress.page = page

    return save(book)

def mark_as_read(id: int, read: bool):
    book = get_book_by_id(id)

    book.reading_progress.read = read

    return save(book)
