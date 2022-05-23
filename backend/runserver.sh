#!/bin/sh

python manage.py collectstatic --no-input
python manage.py migrate
gunicorn app.wsgi:application --bind 0.0.0.0:8000