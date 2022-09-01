# Functional test is the user environment
from typer.testing import CliRunner
from car_rental.cli import main

runner = CliRunner()

def test_add_car():
    result = runner.invoke(
        main, ["add", "Opala", "GM", "sedan", 1900, 100, 6]
    )
    assert result.exit_code == 0
