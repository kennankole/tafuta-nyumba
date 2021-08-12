import pytest 
from app import create_app 

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
           pass 
        yield testing_client