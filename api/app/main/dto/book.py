from flask_restx import Namespace, fields
from app.main.dto.bookprocess import BookProcess
from app.main.dto.readingprogress import ReadingProgress
from app.main.dto.metadata import Metadata

class BookDto:
    api = Namespace('book', description='book related operations')

    get_book = api.model('get_book', {
        'id': fields.Integer(),
        'cover_image': fields.String(),
        'file_id': fields.String(),
        'num_pages': fields.Integer(),
        'cover_image': fields.String(),
        'book_process': fields.Nested(BookProcess.get_bookprocess),
        'reading_progress': fields.Nested(ReadingProgress.get_readingprogress),
        'meta': fields.List(fields.Nested(Metadata.get_metadata))
    })
