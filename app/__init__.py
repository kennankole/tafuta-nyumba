from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

# Globally accessible variables
db = SQLAlchemy()
redis = FlaskRedis()


def create_app():
    ''' Initialize the core of the app'''
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app.views import views

        app.register_blueprint(views) 

        return app