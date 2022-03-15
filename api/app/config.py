import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

def get_postgres_uri():
    db_user = os.getenv('DB_USER', '')
    db_password = os.getenv('DB_PASSWORD', '')
    db_host = os.getenv('DB_HOST', '')
    db_name = os.getenv('DB_NAME', '')
    template_string = 'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}'

    return template_string.format(
            db_user=db_user,
            db_password=db_password,
            db_host=db_host,
            db_name=db_name)

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False
    # Swagger
    RESTX_MASK_SWAGGER = False
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    BOOKS_PROCESSING_FOLDER='uploads/processing'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = get_postgres_uri() 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def get_config(env_name):
    if env_name == "development":
        return DevelopmentConfig
    elif env_name == 'production':
        return ProductionConfig
