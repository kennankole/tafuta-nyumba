import os

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


uri = "postgresql://voavcpovmoccjx:d9e5d1d6bae8f9eeed4c61a052b1770fa50845646a016f67250daa397b09f5b4@ec2-34-204-226-228.compute-1.amazonaws.com:5432/dd9430bj1tc15v"


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY") or "AS SECRET KEY"
    DATABASE = os.getenv("DATABASE")
    TESTING = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"
    USER = os.getenv("USER")
    APP_NAME = os.environ.get("APP_NAME")
    API_KEY = config("API_KEY", default="qwerty")
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")
    REDIS_URL = config("REDIS_URL", default="localhost")
    REDIS_DB = os.environ.get("REDIS_DB")
    REDISTOGO_URL = os.getenv("REDISTOGO_URL", default="localhost")
    if uri and uri.startswith("postgres://"):
        uri.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = uri


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = uri
