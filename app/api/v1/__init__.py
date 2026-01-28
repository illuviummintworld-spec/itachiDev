"""API v1 module"""
from fastapi import APIRouter
from app.api.v1 import email

api_router = APIRouter()
api_router.include_router(email.router, prefix="/email", tags=["Email Intelligence"])
