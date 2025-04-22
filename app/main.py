# main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Training(BaseModel):
    distance_km: float
    pace_min_per_km: float
    notes: str

@app.post("/training")
def create_training(training: Training):
    return {
        "message": "Entrenamiento recibido correctamente",
        "data": training.model_dump()
    }