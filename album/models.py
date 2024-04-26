from utils.uuid_utils import upload_to_rename
from django.db import models


class MediaItem(models.Model):

    path = models.FileField(upload_to=upload_to_rename, null=False, blank=False)
    extension = models.CharField(max_length=4, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.path)


class Album(models.Model):
    
    title = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title