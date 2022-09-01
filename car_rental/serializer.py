from datetime import datetime
from pydantic import BaseModel

class Car_Out(BaseModel):
    # Optional is a optional number in the database because is a primary key
    name: str
    model: str
    category: str
    year: int
    price: int
    rate: int
    date: datetime

class Car_In(BaseModel):
    # Optional is a optional number in the database because is a primary key
    name: str
    model: str
    category: str
    year: int
    price: int
    rate: int
    date: datetime