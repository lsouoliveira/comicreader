from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rest_paginate import Pagination

from .config import config_by_name
from flask.app import Flask

db = SQLAlchemy()
pagination = Pagination()

def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.config['PAGINATE_PAGINATION_OBJECT_KEY'] = "pagination"
    app.config['PAGINATE_DATA_OBJECT_KEY'] = "data"

    db.init_app(app)

    return app
