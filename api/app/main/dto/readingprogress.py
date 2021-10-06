from flask_restx import Namespace, fields

class ReadingProgress:
    api = Namespace('readingprogress', description='book reading progress')

    get_readingprogress = api.model('get_readingprogress', {
        'page': fields.Integer(),
        'read': fields.Boolean(),
        'updated_at': fields.Date()
    })
