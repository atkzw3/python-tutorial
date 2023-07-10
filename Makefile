build:
	docker compose up -d --build
up:
	docker-compose up -d
down:
	docker-compose down
app:
	docker-compose exec app bash

