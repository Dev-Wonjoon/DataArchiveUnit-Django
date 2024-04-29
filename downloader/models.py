from django.db import models
from album.models import MediaItem


class Url(models.Model):
    
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255, null=False, blank=False, unique=True)
    site = models.CharField(max_length=16, null=True, blank=True)
    media = models.OneToOneField(MediaItem, on_delete=models.CASCADE)
