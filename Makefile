install:
	(pip install -U pip poetry;\
	poetry install)
install-hooks:
	cp .pre-push .git/hooks/pre-push
lint:
	(poetry run mypy app/ && \
    poetry run flake8 && \
    poetry run black .; \
	poetry run isort --profile black .)
format:
	(poetry run black .; \
	poetry run isort --profile black .)
test:
	poetry run pytest tests
