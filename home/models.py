from django.db import models

import uuid
import os
import secrets
import string

# Create your models here.


class Folder(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)


def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)


class Files(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_path)
    created_at = models.DateField(auto_now=True)


class Textdata(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
    set_duration = models.DurationField()


class PublicText(models.Model):
    text = models.OneToOneField(Textdata, on_delete=models.CASCADE)


class PublicFiles(models.Model):
    files = models.OneToOneField(Folder, on_delete=models.CASCADE)


class PrivateText(models.Model):
    text = models.OneToOneField(Textdata, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_unique_token()
        super().save(*args, **kwargs)

    def generate_unique_token(self):
        characters = string.ascii_letters + string.digits
        while True:
            token = "".join(secrets.choice(characters) for _ in range(6))
            if not PrivateText.objects.filter(token=token).exists():
                return token


class PrivateFiles(models.Model):
    files = models.OneToOneField(Folder, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_unique_token()
        super().save(*args, **kwargs)

    def generate_unique_token(self):
        characters = string.ascii_letters + string.digits
        while True:
            token = "".join(secrets.choice(characters) for _ in range(6))
            if not PrivateFiles.objects.filter(token=token).exists():
                return token
