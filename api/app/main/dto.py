from flask_restx import Namespace, fields

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
        'read': fields.Boolean(),
        'updated_at': fields.Date()
    })

class BookDto:
    api = Namespace('book', description='book related operations')

    bookmark = api.model('bookmark', {
        'page': fields.Integer(required=True)
    })

    get_book = api.model('get_book', {
        'id': fields.Integer(),
        'cover_image': fields.String(),
        'num_pages': fields.Integer(),
        'cover_image': fields.String(),
        'book_process': fields.Nested(BookProcessDto.get_bookprocess),
        'reading_progress': fields.Nested(ReadingProgressDto.get_readingprogress),
        'meta': fields.List(fields.Nested(MetadataDto.get_metadata))
    })
