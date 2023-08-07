include .env
export

run:
	@poetry run python ./orderparser/manage.py runserver

makemigrations:
	@poetry run python ./orderparser/manage.py makemigrations

migrate:
	@poetry run python ./orderparser/manage.py migrate

admin-create:
	@poetry run python ./orderparser/manage.py createsuperuser --username admin --email admin@admin.admin --skip-checks

makemigrate: makemigrations migrate
	@echo Make and do migrations
