from flask_restx import Api
from flask import Blueprint

from .main.controller.test_controller import api as test_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='COMIC READER API',
    version='1.0',
    description='Comic Reader API.'
)

api.add_namespace(test_ns, path="/")
