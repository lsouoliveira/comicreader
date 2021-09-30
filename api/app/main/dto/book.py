from flask_restx import Namespace, fields

class BookDto:
    api = Namespace('book', description='book related operations')

    get_book = api.model('get_book', {
        'id': fields.Integer(),
        'cover_image': fields.String(),
        'file_id': fields.String(),
        'num_pages': fields.Integer(),
        'cover_image': fields.String()
    })
