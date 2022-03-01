import os
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_cors import CORS

import json
from celery import Celery
from config import Config


db = SQLAlchemy()
manager = Manager()
migrate = Migrate()
celery = Celery(
        __name__,
        broker=Config.CELERY_BROKER_URL,
        result_backend=Config.CELERY_RESULT_BACKEND)

def create_app() -> Flask:
    app = Flask(__name__)

    CONFIG_TYPE = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(CONFIG_TYPE)

    celery.conf.update(app.config)

    initialize_extensions(app)
    register_blueprints(app) 

    return app

def initialize_extensions(app):
    db.init_app(app)

    migrate.init_app(app, db)

    @app.after_request
    def after_request(response):
        response.headers.add('Content-Type', 'application/json')
        response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')

        if int(response.status_code) >= 400:
            try:
                response_data = json.loads(response.get_data())

                response_data.pop('message', None)

                response.set_data(json.dumps(response_data))
            except:
                pass

        return response


def register_blueprints(app):
    from .main import main_blueprint

    app.register_blueprint(main_blueprint, url_prefix="/v1")
