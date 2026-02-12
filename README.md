# TODO REST API

A minimal TODO management REST API built with FastAPI, SQLAlchemy, and SQLite.

## Setup

```bash
pip install -r requirements.txt
```

## Run the server

```bash
uvicorn app.main:app
```

The API will be available at `http://127.0.0.1:8000`.

## Run tests

```bash
pytest
```

## API Endpoints

| Method | Path            | Description   |
|--------|-----------------|---------------|
| GET    | /health         | Health check  |
| POST   | /todos          | Create a todo |
| GET    | /todos          | List all todos|
| GET    | /todos/{id}     | Get a todo    |
| PATCH  | /todos/{id}     | Update a todo |
| DELETE | /todos/{id}     | Delete a todo |
