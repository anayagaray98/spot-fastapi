from fastapi.testclient import TestClient
from .main import app
"""Defining some testing procedures"""
#_______________________________________________________
client = TestClient(app)
#______________________________________________________
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}