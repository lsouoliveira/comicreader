from flask_restx import Namespace, fields
from flask import url_for, request
from app.models import BookType 

class CustomUrl(fields.Raw):
    def __init__(self, endpoint=None, absolute=False, **kwargs):
        super(CustomUrl, self).__init__(**kwargs)
        self.endpoint = endpoint
        self.absolute = absolute

    def format(self, value):
        endpoint = self.endpoint if self.endpoint else request.endpoint
        return url_for(endpoint, id=value, _external=self.absolute) 

class BookProcessDto:
    api = Namespace('bookprocess', description='book processing status')

    get_bookprocess = api.model('get_bookprocess', {
        'error_code': fields.Integer(),
        'status': fields.String(),
        'file_id': fields.String()
    })

class MetadataDto:
    api = Namespace('metadata', description='book metadata')

    get_metadata = api.model('get_metadata', {
        'key': fields.String(),
        'value': fields.String(),
        'data_type': fields.String()
    })

class ReadingProgressDto:
    api = Namespace('readingprogress', description='book reading progress')

    get_readingprogress = api.model('get_readingprogress', {
        'page': fields.Integer(),
        'percent': fields.Float(),
        'read': fields.Boolean(),
        'updated_at': fields.Date()
    })

class BookDto:
    api = Namespace('book', description='book related operations')

    bookmark = api.model('bookmark', {
        'page': fields.Integer(required=True),
        'percent': fields.Float(required=True)
    })

    get_book = api.model('get_book', {
        'id': fields.String(),
        'num_pages': fields.Integer(),
        'book_type': fields.String(),
        'cover_image': CustomUrl(endpoint='main.image_image', absolute=True),
        'book_process': fields.Nested(BookProcessDto.get_bookprocess),
        'reading_progress': fields.Nested(ReadingProgressDto.get_readingprogress),
        'meta': fields.List(fields.Nested(MetadataDto.get_metadata))
    })
