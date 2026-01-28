"""Database models"""
from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from datetime import datetime, UTC

class User(Base):
    """User model for authentication"""
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

class EmailVerification(Base):
    """Email verification results"""
    __tablename__ = "email_verifications"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), index=True, nullable=False)
    status = Column(String(50), nullable=False)  # valid, invalid, unknown
    smtp_check = Column(Boolean, default=False)
    disposable = Column(Boolean, default=False)
    breach_found = Column(Boolean, default=False)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))

class ScanResult(Base):
    """Generic scan results"""
    __tablename__ = "scan_results"
    
    id = Column(Integer, primary_key=True, index=True)
    scan_type = Column(String(50), nullable=False)  # email, domain, social, etc.
    target = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)  # pending, completed, failed
    result_data = Column(Text, nullable=True)
    user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
    completed_at = Column(DateTime, nullable=True)
