from flask_restx import Namespace, fields

class BookProcessDto:
    api = Namespace('bookprocess', description='book processing status')

    get_bookprocess = api.model('get_bookprocess', {
        'error_code': fields.Integer(),
        'status': fields.String()
    })
