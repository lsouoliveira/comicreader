from app.main import db
from app.main.model.book import Book

def find():
    return Book.query

def find_by_id(id):
    return Book.query.filter_by(id=id).first()
