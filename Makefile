install:
	uv sync

start:
	uv run game

lint:
	uv run ruff check

test:
	uv run pytest -v