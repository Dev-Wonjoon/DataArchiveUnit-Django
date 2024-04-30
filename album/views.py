from django.shortcuts import render
from django.views.generic import ListView
from .models import MediaItem

class MediaListView(ListView):
    template_name = 'album/index.html'
    context_object_name = 'media_list'
    model = MediaItem