"""Test configuration and fixtures"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)

@pytest.fixture
def sample_email():
    """Sample email for testing"""
    return "test@example.com"
