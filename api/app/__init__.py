from flask_restx import Api
from flask import Blueprint

from .main.controller.v1.book_controller import api as book_ns
from .main.controller.v1.bookprocess_controller import api as bookprocess_ns
from .main.controller.v1.readingprogress_controller import api as readingprogress_ns
from .main.controller.v1.metadata_controller import api as metadata_ns

api_blueprint = Blueprint('api', __name__)

api = Api(
    api_blueprint,
    title='COMIC READER API',
    version='1.0',
    description='Comic Reader API.'
)

api.add_namespace(book_ns, path="/books")
api.add_namespace(bookprocess_ns, path="/book-processes")
api.add_namespace(readingprogress_ns, path="/reading-progresses")
api.add_namespace(metadata_ns, path="/metadatas")
