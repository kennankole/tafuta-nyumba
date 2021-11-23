import os
import psycopg2

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))




class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL?sslmode=require")
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

   
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

class ProductionConfig(Config):
    pass
