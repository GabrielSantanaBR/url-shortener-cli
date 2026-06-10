import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "API is working"
    }

def test_shorten_url():

    response = client.post(
        "/shorten",
        json={
            "url": "https://www.google.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert "code" in data["data"]

def test_invalid_url():

    response = client.post(
        "/shorten",
        json={
            "url": "google"
        }
    )

    assert response.status_code == 400