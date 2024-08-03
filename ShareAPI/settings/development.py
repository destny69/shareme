from .base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r(!5$!$(%d6!%-sw)gh87al-ll&xt=%1#lb3@qye48ok-@*)4q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "http://206.189.140.178:8080/",
    "206.189.140.178",
    "rdxshare.tech",
    "*",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"

CELERY_BROKER_URL = "redis://localhost:6381/0"
CELERY_RESULT_BACKEND = "redis://localhost:6381/0"
