import re
from fastapi import FastAPI, Request
from pydantic import BaseModel, ValidationError
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

class InputText(BaseModel):
    text: str

# Patrón muy básico para detectar palabras SQL comunes (puedes ampliar según necesites)
SQL_PATTERN = re.compile(
    r"(select|insert|update|delete|drop|truncate|--|;|\/\*|\*\/|union|alter|create|exec|declare)\b",
    re.IGNORECASE
)

@app.post("/response")
async def responder(request: Request):
    try:
        input_data = InputText.parse_obj(await request.json())
    except ValidationError:
        return JSONResponse(
            status_code=422,
            content={"detail": "Invalid input. Expecting JSON with 'text' field."}
        )
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"detail": "Bad request. Please send a valid JSON body."}
        )

    # Detectar posible código SQL
    if SQL_PATTERN.search(input_data.text):
        return JSONResponse(
            status_code=400,
            content={"detail": "Input contains forbidden SQL keywords or patterns."}
        )

    response_text = input_data.text + " | Default response"
    timestamp = datetime.utcnow().isoformat() + "Z"

    return {
        "text": input_data.text,
        "response": response_text,
        "timestamp": timestamp
    }

@app.get("/")
async def root():
    return "service working"

asgi_app = app
