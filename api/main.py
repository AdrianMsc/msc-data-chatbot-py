import re
from fastapi import FastAPI, Request
from pydantic import BaseModel, ValidationError
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

# ✔️ Modelo actualizado con id y sender
class InputText(BaseModel):
    id: int
    sender: str
    text: str

# SQL PATTERN DETECTION (solo consultas estructuradas)
SQL_PATTERN = re.compile(
    r"""
    (
        (select\s.+\sfrom\s.+) |                    
        (insert\s+into\s.+\svalues\s*\(.+\)) |     
        (update\s+.+\sset\s.+) |                    
        (delete\s+from\s.+)                         
    )
    """,
    re.IGNORECASE | re.VERBOSE | re.DOTALL
)

@app.get("/")
async def root():
    return {
        "response": "Hello chickens!"
    }

@app.post("/response")
async def responder(request: Request):
    try:
        input_data = InputText.parse_obj(await request.json())
    except ValidationError:
        return JSONResponse(
            status_code=422,
            content={"detail": "Invalid input. Expecting JSON with 'id', 'sender', and 'text' fields."}
        )
    except Exception:
        return JSONResponse(
            status_code=400,
            content={"detail": "Bad request. Please send a valid JSON body."}
        )

    if SQL_PATTERN.search(input_data.text):
        return JSONResponse(
            status_code=400,
            content={"detail": "Input contains forbidden SQL keywords or patterns."}
        )

    response_text = input_data.text + " | Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    timestamp = datetime.utcnow().isoformat() + "Z"

    return {
        "id": input_data.id,
        "sender": input_data.sender,
        "text": input_data.text,
        "content": response_text,
        "timestamp": timestamp
    }

# ASGI app for Vercel
asgi_app = app
