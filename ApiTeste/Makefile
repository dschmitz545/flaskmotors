clean:
	@find ./ -name '*.pyc' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf *__pycache__
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']

init_db:
	FLASK_APP=flaskmotors/app.py flask create-db

format:
	isort **/*.py
	black -l 79 **/**.py

test:
	FLASK_ENV=test pytest tests/ -v --cov=flaskmotors

run_dev:
	FLASK_APP=flaskmotors/app.py FLASK_ENV=development flask run

run:
	FLASK_APP=flaskmotors/app.py FLASK_ENV=development flask run
