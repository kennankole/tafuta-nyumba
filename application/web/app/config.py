import os
from dotenv import load_dotenv

from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

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
    
    CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
    CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
    API_URL = os.environ.get('API_URL')
    BUSINESS_SHORT_CODE = os.environ.get('BUSINESS_SHORT_CODE')
    PASS_KEY = os.environ.get("PASS_KEY")
    STK_PUSH_URL = os.environ.get("STK_PUSH_URL")
    TRANSACTION_TYPE = os.environ.get("TRANSACTION_TYPE")
    API_ENVIRONMENT = "sandbox"
    API_SECRET = os.environ.get("CONSUMER_SECRET")
    API_KEY = os.environ.get("CONSUMER_KEY")
    
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', None)
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', None)
    GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)


class TestConfigs(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/real_estate.db"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = uri
