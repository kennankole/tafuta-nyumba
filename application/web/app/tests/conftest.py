import pytest
from app import create_app, db
from mixer.backend.flask import mixer
from app.config import TestConfigs




@pytest.fixture
def client():
    app = create_app(test_config=True)
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as testing_client:
        with app.app_context():
            db.init_app(app)
            mixer.init_app(app)
            db.create_all()
        yield testing_client
