# Arquivo de modelagem de dados

from datetime import datetime
from typing import Optional
from pydantic import validator
from sqlmodel import SQLModel, Field
from sqlmodel import select


class Car(SQLModel, table=True):
    #Optional is a optional number in the database because is a primary key
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    model: str
    category: str
    year: int
    price: int
    rate: int
    date: datetime = Field(default_factory=datetime.now)

    @validator("rate")
    def validate_ratings(cls, value, field):
        if value < 1 or value > 10:
            raise RuntimeError(f"{field.name} must be between in 1 and 10")
        return value

    @validator("price")
    def validate_cost(cls, value, field):
        if value < 0:
            raise RuntimeError(f"{field.name} must be positive")
        return value


    @validator("year")
    def validate_year(cls, value, field):
        if value < 1890 or value > 2030:
            raise RuntimeError(f"{field.name} must be between in 1890 and 2030")
        return value


