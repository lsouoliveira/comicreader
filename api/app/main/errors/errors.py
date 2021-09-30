from flask import Blueprint, jsonify
import traceback

from ..exceptions.exceptions import InternalError, PageNotFoundError

errors = Blueprint('errors', __name__)

def create_error_response(error):
    payload = {
                'errors': [
                    error.to_dict()
                ]
            }
    return jsonify(payload), error.status_code

@errors.app_errorhandler(404)
def handle_page_not_found(error):
    return create_error_response(PageNotFoundError())

@errors.app_errorhandler(Exception)
def handle_unknown_error(error):
    print(traceback.format_exc())
    return create_error_response(InternalError())

