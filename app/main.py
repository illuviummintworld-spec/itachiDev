from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, UTC
from contextlib import asynccontextmanager
from app.api.v1 import api_router
from app.config import settings
from app.database import init_db
from app.schemas import HealthResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown"""
    # Startup
    try:
        init_db()
    except Exception as e:
        # Log the error but don't fail startup
        # This allows the app to run without a database for testing
        print(f"Warning: Database initialization failed: {e}")
        print("API will run but database operations will fail")
    yield
    # Shutdown
    pass

app = FastAPI(
    title="OSINT Intelligence Platform",
    version="1.0.0",
    description="Advanced OSINT & Cybersecurity Intelligence Platform",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/health", tags=["Health"], response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "timestamp": datetime.now(UTC)
    }

@app.get("/metrics", tags=["Monitoring"])
async def metrics():
    """Prometheus metrics endpoint"""
    return {"message": "Metrics endpoint - integrate prometheus_client for full metrics"}