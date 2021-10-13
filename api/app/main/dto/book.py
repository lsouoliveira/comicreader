from flask_restx import Namespace, fields
from app.main.dto.bookprocess import BookProcessDto
from app.main.dto.readingprogress import ReadingProgressDto
from app.main.dto.metadata import MetadataDto

class BookDto:
    api = Namespace('book', description='book related operations')

    bookmark = api.model('bookmark', {
        'page': fields.Integer(required=True)
    })

    get_book = api.model('get_book', {
        'id': fields.Integer(),
        'cover_image': fields.String(),
        'file_id': fields.String(),
        'num_pages': fields.Integer(),
        'cover_image': fields.String(),
        'book_process': fields.Nested(BookProcessDto.get_bookprocess),
        'reading_progress': fields.Nested(ReadingProgressDto.get_readingprogress),
        'meta': fields.List(fields.Nested(MetadataDto.get_metadata))
    })
