"""
Simple API Key authentication utility.
"""
from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import settings
from utils.logger import get_logger

# Create logger for authentication
auth_logger = get_logger("auth")

# Security scheme
security = HTTPBearer()

def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)) -> bool:
    """
    Verify the provided API key.
    
    Args:
        credentials: The HTTP authorization credentials
        
    Returns:
        bool: True if API key is valid
        
    Raises:
        HTTPException: If API key is invalid or missing
    """
    if credentials.scheme != "Bearer":
        auth_logger.warning("Invalid authentication scheme", scheme=credentials.scheme)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme. Use Bearer token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    if credentials.credentials != settings.API_KEY:
        auth_logger.warning("Invalid API key attempted", 
                          key_prefix=credentials.credentials[:8] + "..." if credentials.credentials else "None")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    auth_logger.debug("API key verified successfully")
    return True

def get_api_key(credentials: HTTPAuthorizationCredentials = Security(security)) -> str:
    """
    Get and verify API key, return the key if valid.
    
    Args:
        credentials: The HTTP authorization credentials
        
    Returns:
        str: The verified API key
    """
    verify_api_key(credentials)
    return credentials.credentials