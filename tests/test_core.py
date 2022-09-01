# Executar o pytest -v --disable-warnings
from car_rental.core import add_car_to_database, remove_car_from_database, get_cars_from_database

def test_add_car_to_database():
    assert add_car_to_database("Teste","Teste","tesste",1990,100,8)

def test_get_cars_from_database():
    assert len(get_cars_from_database()) > 0

#def test_remove_car_from_database():
#    assert remove_car_from_database(id=)