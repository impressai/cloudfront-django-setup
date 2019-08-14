from django.db import models
from django.conf import settings

# Create your models here.
class HttpDog(models.Model):
    code = models.CharField(max_length=256, null=False, blank=False)
    phrase = models.CharField(max_length=256, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    spec_title = models.CharField(max_length=256, null=False, blank=False)
    spec_href = models.URLField(max_length=256, null=False, blank=False)
    is_heading = models.BooleanField(default=False, blank=False)
    image = models.ImageField(upload_to='images', default='images/icon-dog.png')

    def __unicode__(self):
        return "{0} {1}".format(self.code, self.phrase)

    def __str__(self):
        return "{0} {1}".format(self.code, self.phrase)