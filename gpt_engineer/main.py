import os
import json
import pathlib
import typer

from flask import Request  # Import the 'Request' object from Flask

from gpt_engineer.chat_to_files import to_files
from gpt_engineer.ai import AI
from gpt_engineer.steps import STEPS
from gpt_engineer.db import DB, DBs


app = typer.Typer()


@app.command()
def chat(
    project_path: str = typer.Argument(str(pathlib.Path(os.path.curdir) / "example"), help="path"),
    run_prefix: str = typer.Option(
        "",
        help="run prefix, if you want to run multiple variants of the same project and later compare them",
    ),
    model: str = "gpt-4",
    temperature: float = 0.1,
    steps_config: str = "default",
    request: Request = None,  # Add the 'request' parameter with a default value of None
):
    app_dir = pathlib.Path(os.path.curdir)
    input_path = project_path
    memory_path = pathlib.Path(project_path) / (run_prefix + "memory")
    workspace_path = pathlib.Path(project_path) / (run_prefix + "workspace")

    ai = AI(
        model=model,
        temperature=temperature,
    )

    dbs = DBs(
        memory=DB(memory_path),
        logs=DB(memory_path / "logs"),
        input=DB(input_path),
        workspace=DB(workspace_path),
        identity=DB(app_dir / "identity"),
    )

    for step in STEPS[steps_config]:
        if step == 'execute_entrypoint':
            # If the step is execute_entrypoint and the 'request' parameter is provided, pass it to the step
            if request:
                messages = step(ai, dbs, request=request)
            else:
                messages = step(ai, dbs)
        else:
            messages = step(ai, dbs)

        dbs.logs[step.__name__] = json.dumps(messages)

if __name__ == "__main__":
    app()
