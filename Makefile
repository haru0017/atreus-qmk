.PHONY: compile flash check format

setup:
	@uv run qmk setup

compile:
	@uv run python tools/qmk_task.py compile

flash:
	@uv run python tools/qmk_task.py flash

check:
	@uv run ruff check . --fix

format:
	@uv run ruff format .
