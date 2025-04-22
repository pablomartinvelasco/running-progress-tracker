# app/models.py

from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Training(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    distance_km: float
    pace_seconds_per_km: float
    notes: str
    date: date = Field(default_factory=date.today)
