from fastapi import APIRouter, HTTPException
from app.services.email_verifier import email_verifier
from app.schemas import EmailRequest, EmailVerificationResponse

router = APIRouter()

@router.post("/verify", response_model=EmailVerificationResponse)
async def verify_email(request: EmailRequest):
    """
    Verify email address using SMTP and additional checks
    
    - **email**: Email address to verify
    
    Returns detailed verification results including:
    - SMTP validation
    - Disposable email detection
    - Domain MX records
    """
    result = email_verifier.verify_smtp(request.email)
    if "error" in result and result["status"] == "unknown":
        raise HTTPException(status_code=500, detail=result.get("error", "Verification failed"))
    return result

@router.post("/predict")
async def predict_email_variations(domain: str, first_name: str, last_name: str):
    """
    Predict possible email variations for a person
    
    - **domain**: Email domain (e.g., company.com)
    - **first_name**: Person's first name
    - **last_name**: Person's last name
    
    Returns common email pattern variations
    """
    variations = [
        f"{first_name.lower()}.{last_name.lower()}@{domain}",
        f"{first_name.lower()}{last_name.lower()}@{domain}",
        f"{first_name[0].lower()}{last_name.lower()}@{domain}",
        f"{first_name.lower()}{last_name[0].lower()}@{domain}",
        f"{last_name.lower()}.{first_name.lower()}@{domain}",
        f"{last_name.lower()}{first_name.lower()}@{domain}",
    ]
    return {"variations": variations}

@router.get("/breaches/{email}")
async def check_breaches(email: str):
    """
    Check if email appears in known data breaches
    
    Note: This requires HIBP API key in production
    """
    return {
        "email": email,
        "breaches_found": False,
        "message": "Breach checking requires HIBP API key configuration"
    }

