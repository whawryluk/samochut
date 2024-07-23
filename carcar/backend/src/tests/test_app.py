import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_create_car(client):
    response = client.post('/api/cars', json={
        "id": "1",
        "engine_type": "gasoline",
        "transmission_type": "manual"
    })
    assert response.status_code == 201
    assert b"Car 1 with gasoline engine and manual transmission created" in response.data

def test_get_car(client):
    client.post('/api/cars', json={
        "id": "2",
        "engine_type": "gasoline",
        "transmission_type": "manual"
    })
    response = client.get('/api/cars/2')
    assert response.status_code == 201
    assert b"engine_status" in response.data