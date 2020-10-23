.PHONY: example test lint format install shell sha256

t test:
	pipenv run pytest .

l lint:
	pipenv run flake8 .

f format:
	pipenv run isort .
	pipenv run black .
	make lint

i install:
	pipenv install

s shell:
	pipenv shell

sha sha256:
	python3 ./sha256

e example:
	python3 . A H red
