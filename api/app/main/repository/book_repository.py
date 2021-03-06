from app import db
from app.models import Book

def save(book):
    db.session.add(book)
    db.session.commit()

    return book

def save_batch(books):
    for book in books:
        db.session.add(book)
    db.session.commit()

def find():
    return Book.query

def find_by_id(id):
    return Book.query.filter_by(id=id).first()
