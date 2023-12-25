import importlib.metadata
from typer.testing import CliRunner
from {{cookiecutter.project_slug}}.cli import cli

def test_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"])
    assert result.exit_code == 0
    version = importlib.metadata.version("{{cookiecutter.project_slug}}")
    assert version in result.output
