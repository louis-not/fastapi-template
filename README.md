# FastAPI Backend Template

A simple FastAPI backend template with basic structure and Docker support.

## Project Structure

```
fastapi-backend-template/
├── app/
│   ├── __init__.py
│   ├── app.py              # Main FastAPI application
│   ├── config.py           # Configuration settings
│   ├── models/             # Pydantic models
│   │   └── __init__.py
│   ├── routes/             # API routes
│   │   ├── __init__.py
│   │   └── items.py        # Sample routes
│   ├── services/           # Business logic
│   │   └── __init__.py
│   ├── infra/              # Infrastructure layer
│   │   └── __init__.py
│   └── utils/              # Utility functions
│       └── __init__.py
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── .env.example          # Environment variables example
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Getting Started

### Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Copy environment variables:
```bash
cp .env.example .env
```

4. Run the application:
```bash
cd app
python app.py
```

The API will be available at `http://localhost:8000`

### Docker Development

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

## API Documentation

- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## Sample Endpoints

- `GET /ping` - Health check
- `GET /` - Root endpoint

## Logger Usage

The template includes a categorized logger utility for easy service-specific logging:

```python
from utils.logger import get_logger

# Create service-specific logger
upload_logger = get_logger("upload")

# Log with context
upload_logger.info("File uploaded", filename="doc.pdf", size=1024, user_id=123)

# Use pre-configured loggers
from utils.logger import server_logger, upload_logger, db_logger, auth_logger
```

### Log Files
- `logs/server.log` - Server-related logs
- `logs/upload.log` - Upload service logs
- `logs/database.log` - Database operation logs
- `logs/[service_name].log` - Custom service logs

### Log Levels
- `DEBUG` - Detailed debugging information
- `INFO` - General information about program execution
- `WARNING` - Something unexpected happened
- `ERROR` - A serious problem occurred
- `CRITICAL` - A very serious error occurred

## Environment Variables

See `.env.example` for available configuration options.

## License

This is a template project for educational purposes.