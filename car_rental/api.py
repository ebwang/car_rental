from typing import List
from fastapi import FastAPI
from car_rental.core import get_cars_from_database, add_car_to_database
from car_rental.serializer import Car_In, Car_Out
from car_rental.models import Car

#Tem que instalar o unicorn que fala o ASGI
# O guvicorn nao e assincrono
api = FastAPI(title="Car Rent")


#Anotacao e usada para expor o endpoint
@api.get("/cars/", response_model=List[Car_Out])
async def list_cars():
    cars = get_cars_from_database()
    return cars

#Qdo vc coloca como Async a thread fica livre para receber requisicoes
@api.post("/cars/", response_model=Car_Out)
async def add_car(car_in: Car_In):
    car = Car(**car_in.dict())
    add_car_to_database(car.name,car.model,car.category,car.year,car.price,car.rate)
    return car