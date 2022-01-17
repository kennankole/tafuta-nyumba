import logging
import os

import redis
from app import config as conf
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


def create_app(test_config=None):
    """Initialize the core of the app"""
    app = Flask(__name__, instance_relative_config=False)

    if test_config is None:
        if app.config["ENV"] == 'development':
            app.config.from_object(conf.DevelopmentConfig)
        if app.config['ENV'] == 'production':
            app.config.from_object(conf.Config)
    if test_config:
        app.config.from_object(conf.TestConfigs)

    db.init_app(app)
    with app.app_context():
        from app.views import views
        from app.houses import routes
        from app.hostels.routes import hostels
        from app.business.routes import business
        
        app.register_blueprint(views)
        app.register_blueprint(routes.bp)
        app.register_blueprint(hostels)
        app.register_blueprint(business)
        
        
        db.create_all()
        migrate.init_app(app, db, render_as_batch=True)

    return app
