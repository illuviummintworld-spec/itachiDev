"""Pydantic schemas for request/response validation"""
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Dict, Any
from datetime import datetime

# Email Schemas
class EmailRequest(BaseModel):
    """Email verification request"""
    email: EmailStr

class EmailVerificationResponse(BaseModel):
    """Email verification response"""
    email: str
    status: str
    smtp_valid: bool
    disposable: bool
    breach_found: bool
    details: Optional[Dict[str, Any]] = None
    
    class Config:
        from_attributes = True

# User Schemas
class UserBase(BaseModel):
    """Base user schema"""
    username: str
    email: EmailStr

class UserCreate(UserBase):
    """User creation schema"""
    password: str

class UserResponse(UserBase):
    """User response schema"""
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Scan Schemas
class ScanRequest(BaseModel):
    """Generic scan request"""
    target: str
    scan_type: str = Field(..., description="Type of scan: email, domain, social")

class ScanResponse(BaseModel):
    """Generic scan response"""
    id: int
    scan_type: str
    target: str
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

# Health Check
class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    version: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
