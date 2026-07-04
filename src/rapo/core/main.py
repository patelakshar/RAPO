import json
import typer

from rapo.core.router import run

app = typer.Typer(
    help="RAPO - Red-team Automated Pen-testing Operator"
)


@app.command()
def scan(target: str):
    """
    Run reconnaissance against a target.
    """
    result = run(target)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    app()
