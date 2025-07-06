import pytest
from app import app  # Importa la aplicación Flask desde app.py
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    # Datos de prueba para un login exitoso
    login_data = {
        'email': 'testuser@example.com',
        'password': 'password123'
    }

    # Realiza una solicitud POST a /login con los datos de prueba
    response = client.post('/login', json=login_data)

    # Verifica que el estado sea 200 OK y que se reciba un token
    assert response.status_code == 200
    response_json = response.get_json()
    assert 'token' in response_json

def test_login_failure(client):
    # Datos de prueba para un login fallido
    login_data = {
        'email': 'testuser@example.com',
        'password': 'wrongpassword'
    }

    # Realiza una solicitud POST a /login con los datos de prueba
    response = client.post('/login', json=login_data)

    # Verifica que el estado sea 401 y que se reciba el mensaje de error
    assert response.status_code == 401
    response_json = response.get_json()
    assert response_json['error'] == 'Credenciales inválidas'
