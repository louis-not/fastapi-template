"""
Logger utility for FastAPI Backend Template.
Provides categorized logging for different services.
"""
import logging
import sys
from typing import Optional
from datetime import datetime
from pathlib import Path

class ServiceLogger:
    """
    A simple logger utility that allows easy categorization by service.
    """
    
    def __init__(self, service_name: str, log_level: str = "INFO"):
        """
        Initialize logger for a specific service.
        
        Args:
            service_name: Name of the service (e.g., "upload", "server", "auth")
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        """
        self.service_name = service_name
        self.logger = logging.getLogger(f"fastapi.{service_name}")
        
        # Set log level
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # Avoid duplicate handlers
        if not self.logger.handlers:
            self._setup_handlers()
    
    def _setup_handlers(self):
        """Setup console and file handlers for the logger."""
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # File handler for service-specific logs
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)
        
        file_handler = logging.FileHandler(
            logs_dir / f"{self.service_name}.log",
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
    
    def debug(self, message: str, **kwargs):
        """Log debug message."""
        self.logger.debug(self._format_message(message, **kwargs))
    
    def info(self, message: str, **kwargs):
        """Log info message."""
        self.logger.info(self._format_message(message, **kwargs))
    
    def warning(self, message: str, **kwargs):
        """Log warning message."""
        self.logger.warning(self._format_message(message, **kwargs))
    
    def error(self, message: str, **kwargs):
        """Log error message."""
        self.logger.error(self._format_message(message, **kwargs))
    
    def critical(self, message: str, **kwargs):
        """Log critical message."""
        self.logger.critical(self._format_message(message, **kwargs))
    
    def _format_message(self, message: str, **kwargs) -> str:
        """Format message with additional context."""
        if kwargs:
            context = " | ".join([f"{k}={v}" for k, v in kwargs.items()])
            return f"{message} | {context}"
        return message


# Pre-configured loggers for common services
def get_logger(service_name: str, log_level: str = "INFO") -> ServiceLogger:
    """
    Get a logger instance for a specific service.
    
    Args:
        service_name: Name of the service
        log_level: Logging level
        
    Returns:
        ServiceLogger instance
    """
    return ServiceLogger(service_name, log_level)


# Common logger instances
server_logger = get_logger("server")
upload_logger = get_logger("upload")
db_logger = get_logger("database")
auth_logger = get_logger("auth")