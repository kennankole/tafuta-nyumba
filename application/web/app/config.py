import os
from decouple import config
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY") or "AS SECRET KEY"
    APP_NAME = os.getenv("APP_NAME")
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"
    # API_KEY = "33995baaac4793c49a4dc158e4feb8d58976bd95b16dd911702aa4172335e484"
    USERNAME = config("USERNAME")
    API_KEY = config("API_KEY")
   