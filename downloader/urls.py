from django.urls import path
from .views import  YoutubeDownloadView


app_name = 'downloader'

urlpatterns = [
    path('', YoutubeDownloadView.as_view(), name='youtube_downloader')
]
