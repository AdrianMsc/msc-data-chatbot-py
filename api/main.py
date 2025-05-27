from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/respuesta")
def responder(input_data: InputText):
    return {"respuesta": input_data.text + " | Respuesta predeterminada"}

# Adaptador para Vercel
# Usa `asgi_app` como punto de entrada
asgi_app = app
