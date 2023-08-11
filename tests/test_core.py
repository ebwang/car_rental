# Executar o pytest -v --disable-warnings
from car_rental.core import (
    add_car_to_database,
    get_cars_from_database,
    remove_car_from_database,
)


def test_add_car_to_database():
    assert add_car_to_database("Teste", "Teste", "tesste", 1990, 100, 8)


def test_get_cars_from_database():
    # USANDO A METODOLIGA AAA
    # ARRANGE -> ARRANJO
    add_car_to_database("Teste", "Teste", "tesste", 1990, 100, 8)
    # ACT - > ATUO
    result = get_cars_from_database()
    # ASSERT -> VALIDO
    assert len(result) > 0


def test_remove_car_to_database():
    assert remove_car_from_database("Teste")
