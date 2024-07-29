#!/bin/sh

if [ "$APP_ENV" = "web" ]; then
    echo "Running Django application..."
    exec gunicorn ShareAPI.wsgi:application --bind 0.0.0.0:8000
elif [ "$APP_ENV" = "worker" ]; then
    echo "Running Celery worker..."
    exec celery -A ShareAPI worker --loglevel=info
elif [ "$APP_ENV" = "beat" ]; then
    echo "Running Celery beat..."
    exec celery -A ShareAPI beat --loglevel=info
else
    echo "Invalid APP_ENV value. Must be 'web', 'worker', or 'beat'."
    exit 1
fi
