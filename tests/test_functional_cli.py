# Functional test is the user environment
from typer.testing import CliRunner
from car_rental.cli import main

runner = CliRunner()

def test_add_car():
    result = runner.invoke(
        main, ["add", "Gala", "GM", "--category=sedan", "--year=1900", "--price=100", "--rate=6"]
    )
    assert result.exit_code == 0

def test_remove_car():
    result = runner.invoke(
        main, ["remove", "Gala"]
    )
    assert result.exit_code == 0

def test_list_cars():
    result = runner.invoke(
        main, ["list"]
    )
    assert result.exit_code == 0