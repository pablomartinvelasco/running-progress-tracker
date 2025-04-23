# app/main.py

from fastapi import FastAPI
from sqlmodel import Session, select
from app.models import Training, TrainingCreate
from app.database import create_db_and_tables, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "Running Progress Tracker API funcionando correctamente"}

@app.post("/training")
def create_training(training_in: TrainingCreate):
    training_data = training_in.dict()
    if training_data["training_date"] is None:
        from datetime import date
        training_data["training_date"] = date.today()
    training = Training(**training_data)
    with Session(engine) as session:
        session.add(training)
        session.commit()
        session.refresh(training)
    return {
        "message": "Entrenamiento guardado en la base de datos",
        "data": training.model_dump()
    }

@app.get("/trainings")
def read_trainings():
    with Session(engine) as session:
        statement = select(Training)
        trainings = session.exec(statement).all()
        return trainings