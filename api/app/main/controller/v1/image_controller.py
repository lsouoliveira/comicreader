from flask_restx import Resource
from flask import send_from_directory, send_file
from flask_restx import Namespace
from app.exceptions import ResourceNotFound

api = Namespace('image', description='image related operations')

@api.route('/<id>')
@api.param('id', 'The image identifier')
class Image(Resource):
    def get(self, id):
        return send_file('../public/images/' + str(id))
