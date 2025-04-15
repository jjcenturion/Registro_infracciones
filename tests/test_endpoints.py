import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
from app.app import app  # archivo principal
from app.repositories import VehiculoRepo
from app.schemas import Vehiculo

client = TestClient(app)

@pytest.fixture
def mock_find_all(monkeypatch):
    mock_vehiculo = Vehiculo(id=1, placa_patente="AH01", marca="Toyota", color="negro", propietario_id=1)
    mock_repo = MagicMock()
    mock_repo.find_all.return_value = [mock_vehiculo]
    
    #Simula el repo 
    monkeypatch.setattr("app.app.VehiculoRepo", lambda: mock_repo)

    #Simula la sesion de la base de datos
    monkeypatch.setattr("app.app.get_db", lambda: MagicMock())
    return mock_repo

def test_get_vehiculos_success(mock_find_all):
    response = client.get("/vehiculos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["marca"] == "Toyota"

