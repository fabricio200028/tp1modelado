from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo del mensaje
class Mensaje(BaseModel):
    id: int
    user: str
    mensaje: str