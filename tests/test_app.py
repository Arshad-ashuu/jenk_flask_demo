import json
import sys
import os

# Add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app   # now this will work

def test_index_route():
    client = app.test_client()
    response = client.get("/")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["status"] == "ok"

def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["status"] == "healthy"
