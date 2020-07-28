import os
import pytest

from application import app

FIXTURE_DIR = os.path.join(os.path.dirname(os.path.dirname((__file__))))

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200