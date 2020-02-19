from django.contrib import admin
from .models import PublicImage, PrivateImage
# Register your models here.

admin.site.register(PublicImage)
admin.site.register(PrivateImage)