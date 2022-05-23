#!/bin/sh

python backend/manage.py collectstatic --no-input
python backend/manage.py migrate
gunicorn backend.app.wsgi:application --bind 0.0.0.0:8055