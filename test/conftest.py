from app import create_app
import pytest


@pytest.fixture
def client():
    app = create_app()
    client = app.test_client()
    return client
