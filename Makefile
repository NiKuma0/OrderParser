-include .env
export

DJANGO_MANAGER ?= ./orderparser/manage.py
GUNICRON ?= python -m gunicorn

create-env:
	@cp -u .env.example .env
run-db:
	sudo docker compose -f infra/docker-pg.yml up -d
run: do-migrate
	$(DJANGO_MANAGER) runserver
run-wsgi: do-migrate collectstatic
	$(GUNICRON) orderparser.core.wsgi:application -c ./gunicorn.conf.py
run-docker-compose: create-env
	sudo docker compose -f infra/docker-compose.yml up -d
run-docker-compose-dev: create-env
	sudo docker compose -f infra/docker-compose.yml up --build
makemigrations:
	$(DJANGO_MANAGER) makemigrations
do-migrate:
	$(DJANGO_MANAGER) migrate
create-admin: do-migrate
	$(DJANGO_MANAGER) createsuperuser --noinput \
		--username $(DJANGO_ADMIN_USERNAME) \
		--email $(DJANGO_ADMIN_EMAIL) \
		--password $(DJANGO_ADMIN_PASSWORD)\
		--skip-checks
migrate: makemigrations migrate
	@echo Make and do migrations
collectstatic:
	$(DJANGO_MANAGER) collectstatic -c --noinput
