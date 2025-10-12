import typer
from typing import Annotated

app = typer.Typer()

@app.command()
def run(prompt: Annotated[list[str], typer.Argument(..., help="Your prompt")]):
    joined_prompt = " ".join(prompt)
    print(f"You said: {joined_prompt}")

if __name__ == "__main__":
    app()

