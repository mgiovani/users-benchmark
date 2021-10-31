VENV=.venv/bin/

install:
	python3 -m venv .venv; \
	source ./.venv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt; \

run-db:
	docker run -p 5432:5432 -e POSTGRES_DB=users_benchmark -e POSTGRES_PASSWORD=abc123 -d postgres -N 1024

run-web:
	$(VENV)uvicorn main:app --workers 8

clean:
	rm -rf .venv;
	find -iname "*.pyc" -delete;
