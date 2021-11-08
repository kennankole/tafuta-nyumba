import os

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.getenv("SECRET_KEY") or "AS SECRET KEY"
    SECRET_KEY = config("SECRET_KEY")
    APP_NAME = config("APP_NAME")
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"
    USERNAME = config("USERNAME")
    API_KEY = config("API_KEY")