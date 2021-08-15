import logging
from re import L
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

# logging
if not logging.DEBUG:
    logging.basicConfig(
        filename="app.log",
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(name)s  %(threadName)s : %(message)s'
    )
logger = logging.getLogger()
# Globally accessible variables
db = SQLAlchemy()
redis = FlaskRedis()

def create_app():
    ''' Initialize the core of the app'''
    app = Flask(__name__, instance_relative_config=False)
    if logging.DEBUG:
        app.config.from_object('config.settings.DevelopmentConfig')
    if not logging.DEBUG:
        app.config.from_object('config.settings.ProductionConfig')

    db.init_app(app)

    with app.app_context():
        from app.views import views

        app.register_blueprint(views) 

        return app