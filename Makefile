VENV=.venv/bin/

install:
	python3 -m venv .venv; \
	source ./.venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements/local.txt; \

runserver:
	$(VENV)python manage.py runserver

migrate:
	$(VENV)python manage.py migrate

run-db:
	docker run -p 5432:5432 -e POSTGRES_DB=users_benchmark -e POSTGRES_PASSWORD=abc123 -d postgres

clean:
	rm -rf .venv;
	find -iname "*.pyc" -delete;

run:
	@make run-db
	@make migrate
	@make run-gthread
