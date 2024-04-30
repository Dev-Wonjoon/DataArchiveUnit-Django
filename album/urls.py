from django.urls import path
from .views import MediaListView


app_name = 'album'

urlpatterns = [
    path('', MediaListView.as_view(), name='index'),
]
