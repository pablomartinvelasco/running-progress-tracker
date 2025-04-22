# app/main.py

from fastapi import FastAPI
from sqlmodel import Session
from app.database import create_db_and_tables, engine
from app.models import Training

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Running Progress Tracker API funcionando correctamente"}

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/training")
def create_training(training: Training):
    with Session(engine) as session:
        session.add(training)
        session.commit()
        session.refresh(training)
    return {
        "message": "Entrenamiento guardado en la base de datos",
        "data": training.model_dump()
    }