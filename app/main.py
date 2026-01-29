from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.email import router as email_router
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email_router, prefix="/api/v1/email", tags=["Email"])

@app.get("/health")
async def health():
    return {"status": "ok"}
