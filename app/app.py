"""
FastAPI Backend Template - Main Application

A simple FastAPI application template with basic endpoints.
"""
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from routes import router as api_router
from utils.logger import server_logger

# Create FastAPI application
app = FastAPI(
    title=settings.APP_TITLE,
    version=settings.APP_VERSION,
    description="FastAPI Backend Template",
)

@app.on_event("startup")
async def startup_event():
    """Initialize application on startup."""
    server_logger.info("Application startup initiated")
    server_logger.info("FastAPI application started successfully", 
                      title=settings.APP_TITLE, 
                      version=settings.APP_VERSION)

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up on shutdown."""
    server_logger.info("Application shutdown initiated")
    server_logger.info("FastAPI application stopped")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router)

# Simple ping endpoint for health checks
@app.get("/ping")
async def ping():
    """
    Health check endpoint to verify the API is running.
    Returns a simple success message.
    """
    server_logger.debug("Health check endpoint called")
    return {"status": "success", "message": "API is running"}

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint that returns basic API information.
    """
    return {
        "message": "FastAPI Backend Template",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }

if __name__ == "__main__":
    # Run the API server using the settings from config.py
    uvicorn.run(
        "app:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )