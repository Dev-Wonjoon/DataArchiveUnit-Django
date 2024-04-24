from django.db import models
from album.models import MediaItem

class Tag(models.Model):
    
    name = models.CharField(max_length=24, null=False)
    mapping = models.ManyToManyField(MediaItem)