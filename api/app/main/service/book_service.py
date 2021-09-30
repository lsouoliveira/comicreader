from app.main.repository.book_repository import find, find_by_id 

def get_all_books():
    return find()

def get_book_by_id(id):
    return find_by_id(id)
