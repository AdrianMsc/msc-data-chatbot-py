from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/response")
def responder(input_data: InputText):
    return {"response": input_data.text + " | Default response"}

# Adaptador para Vercel
# Usa `asgi_app` como punto de entrada
asgi_app = app
