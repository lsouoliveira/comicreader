from flask_restx import Namespace, fields

class BookDto:
    api = Namespace('book', description='book related operations')

    get_book = api.model('get_book', {
    })
