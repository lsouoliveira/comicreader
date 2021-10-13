from app.main import db
from app.main.model.book import Book

def save(book):
    db.session.add(book)
    db.session.commit()

    return book

def find():
    return Book.query

def find_by_id(id):
    return Book.query.filter_by(id=id).first()
