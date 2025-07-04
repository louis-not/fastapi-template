"""
Example service demonstrating logger usage.
"""
from utils.logger import get_logger

# Create a logger for this service
logger = get_logger("example_service")

class ExampleService:
    """Example service with logging."""
    
    def __init__(self):
        self.logger = logger
    
    def process_data(self, data: dict):
        """Example method with logging."""
        self.logger.info("Starting data processing", user_id=data.get("user_id"))
        
        try:
            # Simulate processing
            self.logger.debug("Processing data", data_size=len(data))
            
            # Simulate success
            self.logger.info("Data processing completed successfully", 
                           records_processed=len(data))
            
            return {"status": "success", "processed": len(data)}
            
        except Exception as e:
            self.logger.error("Data processing failed", error=str(e))
            raise
    
    def upload_file(self, filename: str, size: int):
        """Example upload method with logging."""
        upload_logger = get_logger("upload")
        
        upload_logger.info("Starting file upload", filename=filename, size=size)
        
        try:
            # Simulate upload process
            upload_logger.debug("Validating file", filename=filename)
            upload_logger.debug("Writing to storage", size=size)
            
            upload_logger.info("File upload completed", 
                             filename=filename, 
                             size=size, 
                             status="success")
            
            return {"status": "uploaded", "filename": filename}
            
        except Exception as e:
            upload_logger.error("File upload failed", 
                              filename=filename, 
                              error=str(e))
            raise