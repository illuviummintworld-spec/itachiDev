from fastapi import APIRouter, HTTPException
from app.services.email_verifier import email_verifier
from pydantic import BaseModel, EmailStr

router = APIRouter()

class EmailRequest(BaseModel):
    email: EmailStr

@router.post("/verify")
async def verify_email(request: EmailRequest):
    result = email_verifier.verify_smtp(request.email)
    if result["status"] == "unknown":
        raise HTTPException(status_code=500, detail=result.get("error", "Verification failed"))
    return result
