from django.db import models


class Url(models.Model):
    
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255, null=False, blank=False)
    site = models.CharField(max_length=16, null=True, blank=True)