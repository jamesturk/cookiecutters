#!/bin/bash

# the latest versions of our core packages
poetry add --dev pytest pytest-cov mkdocs-material ruff mypy
poetry add structlog
poetry add typer

git init
pre-commit install