from flask import jsonify
from flask import request
from flask_restx import Resource
from flask_restx import Namespace
from typing import Dict, Tuple
from flask_restx import marshal
from flask import send_file

from app import db
from app.main.service.book_service import get_all_books, get_book_by_id, bookmark, mark_as_read
from app.main.service import library_service
from app.main.service import archive_service
from app.main.dto import BookDto, BookProcessDto
from app.main.util.pagination import PaginationUtils
from app.exceptions import EmptyFile

api = BookDto.api 

@api.route('/')
class BookList(Resource):
    @api.doc('list_of_books')
    def get(self):
        """List all books"""
        return PaginationUtils.paginate(
                get_all_books(),
                BookDto.get_book)

    @api.doc("add_books")
    @api.marshal_with(BookDto.get_book, envelope="data")
    def post(self):
        if not "file" in request.files:
            raise EmptyFile()

        uploaded_file = request.files["file"]

        return library_service.add_book(uploaded_file)

@api.route('/<id>/readers/comic/pages/<page_number>')
@api.param('id', 'The book identifier')
@api.param('page_number', 'Page number')
class ComicPage(Resource):
    def get(self, id, page_number):
        image_path = archive_service.get_comic_page(id, int(page_number))
        
        return send_file(image_path)

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
        return bookmark(id, data['page'], data['percent'])

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
