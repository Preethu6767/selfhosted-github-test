# test_app.py

import pytest
from app import app  # Adjust according to your file structure

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.data == b"Hello, World!"
    assert response.status_code == 200
