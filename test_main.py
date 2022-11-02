import pytest
from fastapi.testclient import TestClient
from main import app

mlflow_client = TestClient(app)


def test_read_main():
    response = mlflow_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}