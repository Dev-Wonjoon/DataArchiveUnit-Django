from django.shortcuts import render
from django.views.generic import ListView
from .models import MediaItem

class MediaListView(ListView):
    template_name = 'album/index.html'

    model = MediaItem