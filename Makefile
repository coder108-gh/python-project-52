dev:
		uv run python manage.py runserver

install:
		uv sync


build:
		./build.sh

check:
	 	uv run ruff check .

render-start:
		gunicorn task_manager.wsgi

start:
		uv run gunicorn task_manager.wsgi

migrate:
		uv run python manage.py migrate

create-su:
		uv run python manage.py make_su

