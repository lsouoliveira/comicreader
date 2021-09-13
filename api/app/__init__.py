from flask_restx import Api
from flask import Blueprint

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='COMIC READER API',
    version='1.0',
    description='Comic Reader API.'
)
