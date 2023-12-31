.PHONY: up down recreate test_backend

up:
	docker-compose up -d

down:
	docker-compose down

recreate:
	docker-compose down -v --remove-orphans --volumes
	docker-compose up -d --build --force-recreate

test_backend:
	@cd backend && pytest
