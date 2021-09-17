from flask import request
from flask_restx import Resource
from flask_restx import Namespace
from typing import Dict, Tuple

api = Namespace('book')  

@api.route('/')
class BookList(Resource):
    @api.doc('list_of_books')
    def get(self):
        """List all books"""
        return ''

    def post(self):
        return '' 

@api.route('/<id>')
@api.param('id', 'The book identifier')
class Book(Resource):
    def get(self, id):
        return ''

@api.route('/<id>/bookmark')
@api.param('id', 'The book identifier')
class BookBookmark(Resource):
    def put(self, id):
        return ''

@api.route('/<id>/mark-as-read')
@api.param('id', 'The book identifier')
class BookMarkAsRead(Resource):
    def put(self, id):
        return ''

@api.route('/<id>/mark-as-unread')
@api.param('id', 'The book identifier')
class BookMarkAsUnread(Resource):
    def put(self, id):
        return ''

@api.route('/<id>/metadata')
@api.param('id', 'The book identifier')
class Metadata(Resource):
    def put(self, id):
        return ''