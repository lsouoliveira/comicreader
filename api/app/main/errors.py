from flask import jsonify
import traceback

from . import main_blueprint
from app.exceptions import InternalError, PageNotFoundError, ResourceNotFound

def create_error_response(error):
    payload = {
                'errors': [
                    error.to_dict()
                ]
            }
    return jsonify(payload), error.status_code

@main_blueprint.app_errorhandler(404)
def handle_page_not_found(error):
    return create_error_response(PageNotFoundError())

@main_blueprint.app_errorhandler(ResourceNotFound)
def handle_resource_not_found(error):
    return create_error_response(error)

@main_blueprint.app_errorhandler(400)
def handle_bad_request(error):
    print(error)
    return create_error_response(InternalError())

@main_blueprint.app_errorhandler(Exception)
def handle_unknown_error(error):
    print(traceback.format_exc())
    return create_error_response(InternalError())
