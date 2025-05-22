# Simple Flask Application

This is a basic Flask web application that demonstrates a simple API endpoint and template rendering.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application:

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Available Endpoints

- `GET /`: Home page
- `GET /api/hello`: Returns a JSON response with a greeting message 