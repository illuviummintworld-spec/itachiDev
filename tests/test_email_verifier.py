"""Tests for email verification service"""
import pytest
from app.services.email_verifier import EmailVerifier

def test_email_verifier_initialization():
    """Test EmailVerifier can be initialized"""
    verifier = EmailVerifier()
    assert verifier is not None
    assert len(verifier.disposable_domains) > 0

def test_valid_email_format():
    """Test email format validation"""
    verifier = EmailVerifier()
    assert verifier._is_valid_format("test@example.com") == True
    assert verifier._is_valid_format("user.name@domain.co.uk") == True
    assert verifier._is_valid_format("invalid.email") == False
    assert verifier._is_valid_format("@example.com") == False
    assert verifier._is_valid_format("test@") == False

def test_disposable_email_detection():
    """Test disposable email detection"""
    verifier = EmailVerifier()
    result = verifier.verify_smtp("test@tempmail.com")
    assert result["disposable"] == True
    
def test_invalid_email_format():
    """Test handling of invalid email format"""
    verifier = EmailVerifier()
    result = verifier.verify_smtp("not-an-email")
    assert result["status"] == "invalid"
    assert result["smtp_valid"] == False

def test_mx_record_lookup():
    """Test MX record lookup"""
    verifier = EmailVerifier()
    # Gmail should have MX records
    mx_records = verifier._get_mx_records("gmail.com")
    assert len(mx_records) > 0
    
    # Invalid domain should return empty list
    mx_records = verifier._get_mx_records("this-domain-definitely-does-not-exist-12345.com")
    assert len(mx_records) == 0
