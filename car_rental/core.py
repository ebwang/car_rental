# Arquivo utilizado para a regra de negocio, logica e demais

from typing import Optional, List
from sqlmodel import select
from db import get_session
from models import Car


def add_car_to_database(
    name: str,
    model: str,
    category: str,
    year: int,
    cost: int,
    rate: int
) -> bool:
    with get_session() as session:
        car = Car(**locals())
        session.add(car)
        session.commit()
    return True


#def get_cars_from_database(model: Optional[str] = None) -> List[Car]:
#    with get_session() as session:
#        sql = select(Car)
#        if style:
#            sql = sql.where(Car.style == style)
#        return list(session.exec(sql))