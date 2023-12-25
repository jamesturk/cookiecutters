#!/bin/bash

# the latest versions of our core packages
poetry add --dev pytest pytest-cov black mkdocs-material ruff mypy
poetry add structlog
poetry add typer

pre-commit install