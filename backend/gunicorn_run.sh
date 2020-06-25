#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply master database migrations"
python manage.py migrate

echo "Starting server"
exec gunicorn -w 4 --bind 0.0.0.0:8000 dj.wsgi:application