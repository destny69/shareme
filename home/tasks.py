import logging
from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import Files

logger = logging.getLogger(__name__)


@shared_task
def delete_old_files():
    logger.info("Running task: delete_old_files")
    cutoff_date = timezone.now() - timedelta(minutes=1)  # Adjust the interval as needed
    old_files = Files.objects.all()
    for file in old_files:
        try:
            file.file.delete()  # Delete the file from storage
            file.delete()  # Delete the file record from the database
            logger.info(f"Deleted old file: {file.id}")
        except Exception as e:
            logger.error(f"Error deleting file {file.id}: {e}")


@shared_task
def sum():
    logger.info("Running task: sum")
