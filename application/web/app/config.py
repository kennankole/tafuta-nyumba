import os

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))

# uri = os.getenv("DATABASE_URL")
# if uri.startswith('postgres://'):
#     uri.replace('postgres://', 'postgresql://', 1) 
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:nyumba@localhost/nyumba_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY") or "AS SECRET KEY"
    DATABASE = os.getenv("DATABASE")
    TESTING = os.environ.get("TESTING")
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
    
    
    
