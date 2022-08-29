# Arquivo de frontend cli mas que chama o core para ter inteligencia


import typer
from core import add_car_to_database, get_cars_from_database, remove_car_from_database
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print

main = typer.Typer(help="Car Management Application")
console = Console()

@main.command()
def add(
    name: str,
    model: str,
    category: str,
    year: int,
    price: int,
    rate: int
):
    """Adds a new Car to the database"""
    if add_car_to_database(name, model, category, year, price, rate):
        print(":car: Car added!!!")
    else:
        print(":no_entry: - Cannot add car.")

@main.command("remove")
def remove():
    """Remove car from database"""
    list_cars()
    id = input("Digite o id a ser deletado: ")
    if remove_car_from_database(id):
        print(":car: Car removed!!!")
    else:
        print(":no_entry: - Cannot remove car.")

@main.command("list")
def list_cars(model: Optional[str] = None):
    """Lists Cars from the database"""
    cars = get_cars_from_database(model)
    table = Table(
        title="Car Rent Database" if not model else f"Car Rental {model}"
    )
    headers = [
        "id",
        "name",
        "model",
        "category",
        "year",
        "price",
        "rate",
    ]
    for header in headers:
        table.add_column(header, style="magenta")
    for car in cars:
        car.date = car.date.strftime("%Y-%m-%d")
        values = [str(getattr(car, header)) for header in headers]
        table.add_row(*values)
    console.print(table)