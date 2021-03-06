SHELL := /bin/bash

env:
	cp .env.example .env || exit 0

shell:
	docker-compose exec backend bash

db-create:
	docker-compose exec postgres bash -c 'createdb -U postgres "onecode"'

db-drop:
	docker-compose exec postgres bash -c 'dropdb -U postgres "onecode"'

db-migrate:
	docker-compose run --rm -w /app/ backend poetry run ./backend/manage.py migrate

db-makemigrations:
	docker-compose run --rm -w /app/ backend poetry run ./backend/manage.py makemigrations $(ARGS)
