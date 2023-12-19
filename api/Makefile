.PHONY: setup, enter_container, test, lint, format

setup:
	docker compose down
	docker compose up -d

enter_container:
	docker exec -it api bash

test:
	docker exec api python3 -m poetry run pytest src/tests --cov-report term-missing

lint:
	docker exec api poetry run mypy --explicit-package-bases .
	docker exec api poetry run ruff check .
	docker exec api poetry run black --check .

format:
	docker exec api poetry run ruff check . --fix --exit-non-zero-on-fix
	docker exec api poetry run black .
