"""
Configuration settings for the FastAPI Backend Template.
"""
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings
    
    These settings can be overridden by environment variables.
    """
    # API server settings
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # App metadata
    APP_TITLE: str = "FastAPI Backend Template"
    APP_VERSION: str = "0.1.0"
    
    # CORS settings
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # API Key Authentication
    API_KEY: str = "your-secret-api-key-change-this"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a settings instance
settings = Settings()