from flask import Blueprint, jsonify
import traceback

from ..exceptions.exceptions import InternalError, PageNotFoundError, ResourceNotFound

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

@errors.app_errorhandler(ResourceNotFound)
def handle_resource_not_found(error):
    return create_error_response(error)

@errors.app_errorhandler(400)
def handle_bad_request(error):
    print(error)
    return create_error_response(InternalError())

@errors.app_errorhandler(Exception)
def handle_unknown_error(error):
    print(traceback.format_exc())
    return create_error_response(InternalError())
