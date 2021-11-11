import logging
import os

import redis
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# logging
if not logging.DEBUG:
    logging.basicConfig(
        filename="app.log",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(name)s  %(threadName)s : %(message)s",
    )
logger = logging.getLogger()
# Globally accessible variables
db = SQLAlchemy()
migrate = Migrate()


cache = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379)


def create_app(test_config=None):
    """Initialize the core of the app"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("app.config.Config")
    db.init_app(app)

    with app.app_context():
        from app.views import views

        app.register_blueprint(views)
        db.create_all()
        migrate.init_app(app, db, render_as_batch=True)

        return app
