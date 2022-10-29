# Arquivo de frontend cli mas que chama o core para ter inteligencia

from operator import truediv
import typer
from car_rental.core import (
    add_car_to_database,
    get_cars_from_database,
    remove_car_from_database,
    search_car_from_database
)
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print

#Faz o meu do cli
main = typer.Typer(help="Car Management Application")
#Responsavel pela tabela em modo texto
console = Console()

#Essa anotacao instrui o typer as opcoes do cli
@main.command()
def add(
    name: str,
    model: str,
    category: str = typer.Option(...),
    year: int = typer.Option(...),
    price: int = typer.Option(...),
    rate: int = typer.Option(...),
):
    """Adds a new Car to the database"""
    if add_car_to_database(name, model, category, year, price, rate):
        print(":car: Car added!!!")
    else:
        print(":no_entry: - Cannot add car.")


@main.command("remove")
def remove(name: str):
    """Remove car from database"""
    if remove_car_from_database(name):
        print(":car: Car removed!!!")


@main.command("search")
def search(name: str):
    """Search car from database"""
    if search_car_from_database(name):
        return True



@main.command("list")
#Passa o modelo como Opcional se nao passar vai como none
def list_cars(model: Optional[str] = None):
    """Lists Cars from the database"""
    cars = get_cars_from_database(model)
    table = Table(
        title="Car Rent Database" if not model else f"Car Rental {model}"
    )
    headers = ["id", "name", "model", "category", "year", "price", "rate"]
    for header in headers:
        table.add_column(header, style="magenta")
    for car in cars:
        car.date = car.date.strftime("%Y-%m-%d")
        #Usa-se uma list compreension, na primeira parte converte para string pois na tabela possui tipos diferentes
        #O get attr simplesmente carrega o atributo ou valor atribuido ao valor da coluna ex car.name=Opala
        values = [str(getattr(car, header)) for header in headers]
        table.add_row(*values)
        #O comando de cima vem para subistutir essa estrturua
        # table.add_row(car.name, car.model)
    console.print(table)
