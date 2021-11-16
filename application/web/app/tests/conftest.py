import os
import tempfile

import pytest
from mixer.backend.flask import mixer

from app import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    
    with app.test_client() as testing_client:
        with app.app_context():
            db.init_app(app)
            mixer.init_app(app)
            db.create_all()
        yield testing_client