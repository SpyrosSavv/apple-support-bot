.PHONY: help install lint format

PY := .venv/bin/python

help:  ## Show this help
	@grep -E '^[a-z-]+:.*##' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*## "}; {printf "  %-16s %s\n", $$1, $$2}'

# Setup
install:  ## Create .venv and install app + dev dependencies
	uv venv --python 3.12 .venv
	uv pip install --python $(PY) -r requirements.txt -r requirements-dev.txt

# Quality
lint:  ## Lint and check formatting
	$(PY) -m ruff check .
	$(PY) -m ruff format --check .

format:  ## Auto-format
	$(PY) -m ruff format .
	$(PY) -m ruff check --fix .