import typer

from rapo.core.output import display
from rapo.core.router import run

app = typer.Typer(
    help="RAPO - Red-team Automated Pen-testing Operator"
)


@app.command()
def scan(target: str):
    """
    Run reconnaissance against a target.
    """
    results = run(target)
    display(results)


if __name__ == "__main__":
    app()
