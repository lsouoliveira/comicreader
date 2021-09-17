from flask_restx import Api
from flask import Blueprint

from .main.controller.v1.book_controller import api as book_ns

api_blueprint = Blueprint('api', __name__)

api = Api(
    api_blueprint,
    title='COMIC READER API',
    version='1.0',
    description='Comic Reader API.'
)

api.add_namespace(book_ns, path="/books")
