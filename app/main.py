from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
# Note: We'll create these modules next
# from app.api.v1 import api_router
# from app.config import settings

app = FastAPI(
    title="OSINT Intelligence Platform",
    version="1.0.0",
    description="Advanced OSINT & Cybersecurity Intelligence Platform",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}