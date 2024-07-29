# myapp/tasks.py

from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Files


@shared_task
def delete_old_files():
    cutoff_date = timezone.now() - timedelta(days=30)  # Adjust the interval as needed
    old_files = Files.objects.filter(created_at__lt=cutoff_date)
    for file in old_files:
        file.file.delete()  # Delete the file from storage
        file.delete()  # Delete the file record from the database
