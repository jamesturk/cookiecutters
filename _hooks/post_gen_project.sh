#!/bin/bash

# the latest versions of our core packages
poetry add --dev pytest pytest-cov mkdocs-material ruff mypy
poetry add structlog
poetry add {{ cookiecutter.extra_packages }}

# initialize git repo and install pre-commit hooks
git init
git add .
git commit -m "cookiecutter commit"
pre-commit install
poetry install