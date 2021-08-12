from os import environ

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    API_KEY = environ.get('API_KEY')
    USERNAME = environ.get('USERNAME')
    APP_NAME = environ.get('APP_NAME')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SESSION_TYPE = environ.get('SESSION_TYPE')
    REDIS_URL = environ.get('REDIS_URL')
    REDIS_HOST = environ.get('REDIS_HOST')
    REDIS_PORT = environ.get('REDIS_PORT')
    REDIS_DB = environ.get('REDIS_DB')

    PRODUCT_NAME = environ.get('PRODUCT_NAME')
    PROVIDER_CHANNEL = environ.get('PROVIDER_CHANNEL')

    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TESTING = environ.get('TESTING')