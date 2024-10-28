from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_read_endpoint():
    response = client.get("/endpoint")

    assert response.status_code == 200
    assert response.json() == {"Hello": "Endpoint"}

def test_read_rpc():
    response = client.post(
        "/rpc",
        json={"jsonrpc": "2.0", "method": "sample", "params": None, "id": None}
    )

    assert response.status_code == 200
    assert response.json() == {"jsonrpc": "2.0", "result": {"hello": "world"}, "error": None, "id": None}