start:
	docker compose up -d

stop:
	docker compose stop

rebuild:
	docker compose down
	docker compose pull
	docker compose up -d --build
