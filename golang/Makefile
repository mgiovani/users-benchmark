run-db:
	docker run --name psql_db -p 5432:5432 -e POSTGRES_DB=users_benchmark -e POSTGRES_PASSWORD=abc123 -d postgres

build:
	go build

run:
	chmod +x users_benchmark
	./users_benchmark

exec-db:
	echo "create table users(name varchar(255), email varchar(255), created timestamp, id UUID primary key);"; \
	docker exec -it psql_db psql -U postgres -d users_benchmark
