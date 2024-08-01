"""Console script for three_d_city_model_generator."""
import three_d_city_model_generator

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for three_d_city_model_generator."""
    console.print("Replace this message by putting your code into "
               "three_d_city_model_generator.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
