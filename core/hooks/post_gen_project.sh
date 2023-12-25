#!/bin/bash

# the latest versions of our core packages
poetry add --dev pytest pytest-cov mkdocs-material ruff mypy
poetry add structlog
poetry add typer

git init
git commit -am "cookiecutter: initial commit"
pre-commit install