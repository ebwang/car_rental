# Arquivo de frontend cli mas que chama o core para ter inteligencia


import typer
from core import add_car_to_database
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print

main = typer.Typer(help="Car Management Application")


@main.command()
def add(
    name: str,
    model: str,
    category: str,
    year: int,
    cost: int,
    rate: int
):
    """Adds a new Car to the database"""
    if add_car_to_database(name, model, category, year, cost, rate):
        print(":car: Car added!!!")
    else:
        print(":no_entry: - Cannot add car.")

#@main.command("list")
#def list_cars():
#    """Lists beers from the database"""
