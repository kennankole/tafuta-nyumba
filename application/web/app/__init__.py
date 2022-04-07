import logging
import os
from flask_login import LoginManager

import redis
from app import config as conf
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flask_mpesa import MpesaAPI
from oauthlib.oauth2 import WebApplicationClient

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
mpesa_api = MpesaAPI()
login_manager = LoginManager()

client = WebApplicationClient(conf.Config.GOOGLE_CLIENT_ID)

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
    with app.app_context():
        
        db.init_app(app)
        mpesa_api.init_app(app)
        login_manager.init_app(app)
        
        from app.views import views
        from app.houses import routes
        from app.hostels.routes import hostels
        from app.business.routes import business
        from app.revenue.routes import payment
        from app.dashboard.routes import dashboard
        from app.maps.routes import map
        from app.payment_plan.routes import plan
        from app.auth.routes import auth
        from app.real_estate.routes import home
        
        app.register_blueprint(views)
        app.register_blueprint(routes.bp)
        app.register_blueprint(hostels)
        app.register_blueprint(business)
        app.register_blueprint(payment)
        app.register_blueprint(dashboard)
        app.register_blueprint(map)
        app.register_blueprint(plan)
        app.register_blueprint(auth)
        app.register_blueprint(home)
    
        
        db.create_all()
        migrate.init_app(app, db, render_as_batch=True)

    return app
