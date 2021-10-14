from app.main.repository.book_repository import save, find, find_by_id
from app.exceptions import ResourceNotFound

def save_book(book):
    return save(book)

def get_all_books():
    return find()

def get_book_by_id(id):
    book = find_by_id(id)
    
    if not book:
        raise ResourceNotFound(id)

    return book

def bookmark(id, page):
    book = get_book_by_id(id)

    book.reading_progress.page = page

    return save(book)

def mark_as_read(id, read):
    book = get_book_by_id(id)

    book.reading_progress.read = read

    return save(book)

