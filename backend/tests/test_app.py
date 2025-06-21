import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app

def test_health():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_message():
    client = app.app.test_client()
    response = client.get("/api/message")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from backend!"