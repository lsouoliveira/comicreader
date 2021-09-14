from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(Exception)
def handle_error(error):
    response = {
        'errors': {
            'code': 100
        }
    }

    return jsonify(response), 500
