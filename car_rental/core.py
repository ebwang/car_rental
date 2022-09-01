# Arquivo utilizado para a regra de negocio, logica e demais

from typing import Optional, List
from sqlmodel import select
from car_rental.db import get_session
from car_rental.models import Car


def add_car_to_database(
    name: str, model: str, category: str, year: int, price: int, rate: int
) -> bool:
    with get_session() as session:
        car = Car(**locals())
        session.add(car)
        session.commit()
    return True


def get_cars_from_database(model: Optional[str] = None) -> List[Car]:
    with get_session() as session:
        sql = select(Car)
        if model:
            sql = sql.where(Car.model == model)
        return list(session.exec(sql))


def remove_car_from_database(id) -> bool:
    with get_session() as session:
        sql = select(Car).where(Car.id == id)
        result = session.exec(sql)
        car = result.one()
        session.delete(car)
        session.commit()
    return True
