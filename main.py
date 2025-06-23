from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo del mensaje
class Mensaje(BaseModel):
    id: int
    user: str
    mensaje: str

    # Base de datos temporal (en memoria)
db: List[Mensaje] = []

# GET: todos los mensajes
@app.get("/mensajes", response_model=List[Mensaje])
def obtener_mensajes():
    return db

# GET: mensaje por ID
@app.get("/mensajes/{mensaje_id}", response_model=Mensaje)
def obtener_mensaje(mensaje_id: int):
    for mensaje in db:
        if mensaje.id == mensaje_id:
            return mensaje
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# POST: crear nuevo mensaje
@app.post("/mensajes", response_model=Mensaje)
def crear_mensaje(mensaje: Mensaje):
    for m in db:
        if m.id == mensaje.id:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    db.append(mensaje)
    return mensaje

# PUT: actualizar mensaje por ID
@app.put("/mensajes/{mensaje_id}", response_model=Mensaje)
def actualizar_mensaje(mensaje_id: int, mensaje_actualizado: Mensaje):
    for i, mensaje in enumerate(db):
        if mensaje.id == mensaje_id:
            db[i] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
