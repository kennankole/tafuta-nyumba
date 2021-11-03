from decouple import config


class Config:
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = config("SECRET_KEY") or "AS SECRET KEY"
    APP_NAME = config("APP_NAME")
    STATIC_FOLDER = f"{config('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{config('APP_FOLDER')}/project/media"
    USERNAME = config("USERNAME")
    API_KEY = config("API_KEY")
