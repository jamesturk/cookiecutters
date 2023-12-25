{%- if cookiecutter.cli == "typer" -%}
import importlib.metadata
import logging
import structlog
import typer

cli = typer.Typer()


@cli.command()
def hello(name: str) -> None:
    print(f"Hello {name}")


def _version_callback(value: bool) -> None:
    if value:
        version = importlib.metadata.version("{{ cookiecutter.project_slug }}")
        typer.echo(f"{{ cookiecutter.project_slug }} v{version}")
        raise typer.Exit()


@cli.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show version and exit",
        is_eager=True,
        callback=_version_callback,
    ),
    verbosity: int = typer.Option(
        0, "-v", "--verbose", count=True, help="Verbosity level 0-2"
    ),
) -> None:
    log_level = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}.get(
        verbosity, logging.DEBUG
    )
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
    )


{%- endif %}


if __name__ == "__main__":
    cli()