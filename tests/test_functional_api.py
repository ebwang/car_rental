# Functional test is the user environment
from fastapi.testclient import TestClient

from car_rental.api import api

client = TestClient(api)


def test_list_cars():
    response = client.get("/cars")
    assert response.status_code == 200
    # result = response.json()


# def test_remove_car():
#    response = client.post("/cars")
#    assert response.status_code == 200
#    result = response.json()
