"""
Routes initialization for the FastAPI Backend Template.
"""
from fastapi import APIRouter

# Create main router
router = APIRouter(prefix="/api/v1")

# Include sub-routers