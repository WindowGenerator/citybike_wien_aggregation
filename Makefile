.PHONY: all

CMD := poetry run

INTEGRATION_TESTS := ./tests/integration
UNIT_TESTS := ./tests/unit

all: install-deps pre-commit test

test: test-integration

test-integration:
	$(CMD) pytest -vv $(INTEGRATION_TESTS)

pre-commit:
	$(CMD) pre-commit run --all-files

install-deps:
	@poetry install
	$(CMD) pre-commit install

run:
	$(CMD) python -m src.main