# app/models.py

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class TrainingBase(SQLModel):
    distance_km: float
    pace_seconds_per_km: int
    notes: str
    training_date: Optional[date] = None

class Training(TrainingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    training_date: Optional[date] = Field(default_factory=date.today)

class TrainingCreate(TrainingBase):
    pass