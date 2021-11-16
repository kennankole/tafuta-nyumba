import os
import tempfile

import pytest
from mixer.backend.flask import mixer

from app import create_app, db


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({"TESTING": True, "DATABASE": db_path})
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    
    with app.test_client() as testing_client:
        with app.app_context():
            db.init_app(app)
            mixer.init_app(app)
            db.create_all()
        yield testing_client

    os.close(db_fd)
    os.unlink(db_path)
