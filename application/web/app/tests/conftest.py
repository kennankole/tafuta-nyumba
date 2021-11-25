import pytest
from app import create_app, db
from mixer.backend.flask import mixer

app = create_app(testing=True)


@pytest.fixture
def client():
    with app.test_client() as testing_client:
        with app.app_context():
            db.init_app(app)
            mixer.init_app(app)
            db.create_all()
        yield testing_client
