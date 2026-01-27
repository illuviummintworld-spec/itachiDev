from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "OSINT Intelligence Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Security
    JWT_SECRET_KEY: str = "your-secret-key"
    JWT_ALGORITHM: str = "HS256"
    
    # Database
    DATABASE_URL: str = "postgresql://user:pass@localhost:5432/osint_db"
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # External APIs
    HUNTER_API_KEY: Optional[str] = None
    HIBP_API_KEY: Optional[str] = None
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        env_file = ".env"

settings = Settings()