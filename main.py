from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos
class Mensaje(BaseModel):
    id: int
    user: str
    mensaje: str

# Lista para guardar los mensajes
mensajes = []

# GET: obtener todos los mensajes
@app.get("/mensajes")
def get_mensajes():
    return mensajes

# GET: obtener mensaje por ID
@app.get("/mensajes/{id}")
def get_mensaje(id: int):
    for m in mensajes:
        if m.id == id:
            return m
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# POST: crear nuevo mensaje
@app.post("/mensajes")
def crear_mensaje(mensaje: Mensaje):
    for m in mensajes:
        if m.id == mensaje.id:
            raise HTTPException(status_code=400, detail="Ya existe un mensaje con ese ID")
    mensajes.append(mensaje)
    return mensaje

# PUT: actualizar mensaje por ID
@app.put("/mensajes/{id}")
def actualizar_mensaje(id: int, mensaje_actualizado: Mensaje):
    for i in range(len(mensajes)):
        if mensajes[i].id == id:
            mensajes[i] = mensaje_actualizado
            return mensaje_actualizado
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")

# DELETE: eliminar mensaje por ID
@app.delete("/mensajes/{id}")
def borrar_mensaje(id: int):
    for i in range(len(mensajes)):
        if mensajes[i].id == id:
            del mensajes[i]
            return {"mensaje": "Mensaje eliminado"}
    raise HTTPException(status_code=404, detail="Mensaje no encontrado")
