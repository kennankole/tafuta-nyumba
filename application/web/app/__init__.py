import logging
import os
from urllib.parse import urlparse

import redis
from app import config as conf
from decouple import config
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


cache = redis.from_url(os.environ.get("REDIS_URL", "redis://localhost"))


def create_app(testing=False):
    """Initialize the core of the app"""
    app = Flask(__name__, instance_relative_config=False)

    if app.testing:
        app.config.from_object(conf.TestingConfig)
    else:
        app.config.from_object(conf.Config)

    db.init_app(app)
    with app.app_context():
        from app.views import views

        app.register_blueprint(views)
        db.create_all()
        migrate.init_app(app, db, render_as_batch=True)

        return app
