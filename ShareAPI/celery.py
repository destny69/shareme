from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ShareAPI.settings.development")

app = Celery("ShareAPI")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Add this for periodic task scheduling
app.conf.beat_schedule = {
    "delete-old-files-every-day": {
        "task": "home.tasks.delete_old_files",
        "schedule": 1.0,  # 86400 seconds = 24 hours
    },
    "run_every_sec": {
        "task": "home.tasks.sum",
        "schedule": 1.0,  # 1 second
    },
}

# Fix deprecation warning by ensuring broker retries on startup
app.conf.broker_connection_retry_on_startup = True
