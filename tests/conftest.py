import pytest 


@pytest.fixture
def client():
    from mixer.backend.flask import mixer
    from app import create_app
    app = create_app()
    mixer.init_app(app)
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client