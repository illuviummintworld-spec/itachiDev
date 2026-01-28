"""Tests for email API endpoints"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_email_predict_endpoint():
    """Test email prediction endpoint"""
    response = client.post(
        "/api/v1/email/predict",
        params={
            "domain": "example.com",
            "first_name": "John",
            "last_name": "Doe"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "variations" in data
    assert len(data["variations"]) > 0
    assert "john.doe@example.com" in data["variations"]

def test_email_verify_invalid_format():
    """Test email verification with invalid format"""
    response = client.post(
        "/api/v1/email/verify",
        json={"email": "not-an-email"}
    )
    assert response.status_code == 422  # Validation error

def test_email_breaches_endpoint():
    """Test breach checking endpoint"""
    response = client.get("/api/v1/email/breaches/test@example.com")
    assert response.status_code == 200
    data = response.json()
    assert "email" in data
    assert "breaches_found" in data
