# MSC DATA CHATBOT

[![Python](https://img.shields.io/badge/python-3.11-blue.svg?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.95.2-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Vercel](https://img.shields.io/badge/vercel-black?logo=vercel&logoColor=white)](https://vercel.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Project Description

This is a simple serverless REST API built with FastAPI and deployed on Vercel. It exposes endpoints to:

- Accept a POST request with JSON containing a text string.
- Return a JSON response including the original text, a predefined response message, and a timestamp.
- Detect and reject SQL query patterns in the input text.
- Provide a simple health check GET endpoint.

The API is designed to be minimal, easy to deploy, and scalable via Vercel's serverless platform.

---

## API Documentation

The API exposes the following endpoints:

### POST `/response`

**Description:**  
Accepts JSON with a `text` field, validates it, rejects SQL queries, and responds with an augmented message and timestamp.

**Request Body:**

```json
{
  "text": "your input string"
}
```

**Response:**

```json
{
  "text": "your input string",
  "response": "your input string | Default response",
  "timestamp": "2025-05-27T15:30:00Z"
}
```

**Error Responses:**

- 400 Bad Request: If the input is not valid JSON or is missing the text field.

- 400 Bad Request: If the input contains SQL query patterns.
