from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_endpoint():
    response = client.get("/endpoint")

    assert response.status_code == 200
    assert response.json() == {"Hello": "Endpoint"}