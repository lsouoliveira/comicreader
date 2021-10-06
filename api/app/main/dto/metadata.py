from flask_restx import Namespace, fields

class Metadata:
    api = Namespace('metadata', description='book metadata')

    get_metadata = api.model('get_metadata', {
        'key': fields.String(),
        'value': fields.String(),
        'data_type': fields.String()
    })
