import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_migrate import Migrate

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
migrate = Migrate()

def create_app(test_config=None):
    ''' Initialize the core of the app'''
    app = Flask(__name__, instance_relative_config=False)
    if logging.DEBUG:
        app.config.from_object('config.settings.DevelopmentConfig')
    if not logging.DEBUG:
        app.config.from_object('config.settings.ProductionConfig')

    db.init_app(app)
    redis.init_app(app)

    with app.app_context():
        from app.views import views

        app.register_blueprint(views) 
        db.create_all()
        migrate.init_app(app, db, render_as_batch=True)
        
        return app