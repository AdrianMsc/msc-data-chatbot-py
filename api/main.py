from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/respuesta")
def responder(input_data: InputText):
    respuesta = input_data.text + " | Respuesta predeterminada"
    return {"respuesta": respuesta}

# Vercel requiere que exportemos la variable como "handler"
handler = app
