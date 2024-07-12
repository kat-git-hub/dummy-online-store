install:
	poetry install
lint:
	poetry run flake8 --ignore=E501 tests demoblaze.py
test:
	poetry run python -m unittest discover -s tests