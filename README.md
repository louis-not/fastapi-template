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
- `GET /api/v1/items` - Get all items
- `GET /api/v1/items/{item_id}` - Get specific item
- `POST /api/v1/items` - Create new item

## Environment Variables

See `.env.example` for available configuration options.

## License

This is a template project for educational purposes.