from django.db import models

from http_project.storage_backends import PrivateMediaStorage, PublicMediaStorage

# Create your models here.
class PublicImage(models.Model):
    image = models.ImageField(upload_to="public", storage=PublicMediaStorage())

class PrivateImage(models.Model):
    image = models.ImageField(upload_to="private", storage=PrivateMediaStorage())