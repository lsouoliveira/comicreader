import os
from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import json
from celery import Celery
from app.config import get_config

flask_env = os.getenv('FLASK_ENV', default='development')
current_config = get_config(flask_env)

db = SQLAlchemy()
migrate = Migrate()
celery = Celery(
        __name__,
        broker=current_config.CELERY_BROKER_URL,
        result_backend=current_config.CELERY_RESULT_BACKEND)


def create_app() -> Flask:
    app = Flask(__name__)

    app.config.from_object(current_config)
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
