from flask import request
from flask_restx import Resource
from flask_restx import Namespace
from typing import Dict, Tuple
from app.main import db
from app.main.service.book_service import get_all_books, get_book_by_id, bookmark, mark_as_read
from app.main.dto.book import BookDto
from app.main.dto.bookprocess import BookProcessDto
from app.main.util.pagination import PaginationUtils

api = BookDto.api

@api.route('/')
class BookList(Resource):
    @api.doc('list_of_books')
    def get(self):
        """List all books"""
        return PaginationUtils.paginate(
                get_all_books(),
                BookDto.get_book)

    def post(self):
        return '' 

@api.route('/<id>')
@api.param('id', 'The book identifier')
class Book(Resource):
    @api.marshal_with(BookDto.get_book, envelope="data")
    def get(self, id):
        return get_book_by_id(id)

@api.route('/<id>/bookmark')
@api.param('id', 'The book identifier')
class BookBookmark(Resource):
    @api.expect(BookDto.bookmark, validate=True)
    @api.marshal_with(BookDto.get_book, envelope="data")
    def put(self, id):
        data = request.json
        return bookmark(id, data['page'])

@api.route('/<id>/mark-as-read')
@api.param('id', 'The book identifier')
class BookMarkAsRead(Resource):
    @api.marshal_with(BookDto.get_book, envelope="data")
    def put(self, id):
        return mark_as_read(id, True)

@api.route('/<id>/mark-as-unread')
@api.param('id', 'The book identifier')
class BookMarkAsUnread(Resource):
    @api.marshal_with(BookDto.get_book, envelope="data")
    def put(self, id):
        return mark_as_read(id, False)

@api.route('/<id>/metadata')
@api.param('id', 'The book identifier')
class Metadata(Resource):
    def put(self, id):
        return ''
