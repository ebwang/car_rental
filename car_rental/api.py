from typing import List

from fastapi import FastAPI

from car_rental.core import (
    add_car_to_database,
    get_cars_from_database,
    remove_car_from_database,
)
from car_rental.models import Car
from car_rental.serializer import Car_In, Car_Out

# Tem que instalar o unicorn que fala o ASGI
# O guvicorn nao e assincrono
api = FastAPI(title="Car Rent")


# Anotacao e usada para expor o endpoint
@api.get("/cars", response_model=List[Car_Out])
async def list_cars():
    """
    Endpoint that returns information about all the cars.
    Args:
        Not availible
    Returns:
        The list of all cars
    """
    cars = get_cars_from_database()
    return cars


# Qdo vc coloca como Async a thread fica livre para receber requisicoes
@api.post("/cars", response_model=Car_Out)
async def add_car(car_in: Car_In):
    """
    Endpoint to add cars in database
    Args:
        Name,Model,Category,Year,Price,Rate
    Returns:
        Return the result of add!
    """
    car = Car(**car_in.dict())
    add_car_to_database(
        car.name, car.model, car.category, car.year, car.price, car.rate
    )
    return car


@api.post("/remove_cars", response_model=Car_Out)
async def remove_car(car_in: Car_In):
    """
    Endpoint to remove car
    Args:
        Name
    Returns:
        Return the result of remove!
    """
    car = Car(**car_in.dict())
    remove_car_from_database(car.name)
    return car
