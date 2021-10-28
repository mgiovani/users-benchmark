VENV=.venv/bin/

install:
	python3 -m venv .venv; \
	source ./.venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \

run-db:
	docker run -p 5432:5432 -e POSTGRES_DB=users_benchmark -e POSTGRES_PASSWORD=abc123 -d postgres

migrate:
	$(VENV)python manage.py migrate

run-web:
	$(VENV)gunicorn users_benchmark.wsgi:application -b 0:8000 --log-level DEBUG --workers 8 --worker-class gthread --threads 64

run-default:
	$(VENV)gunicorn users_benchmark.wsgi:application -b 0:8000 --log-level DEBUG --workers 8

clean:
	rm -rf .venv;
	find -iname "*.pyc" -delete;
