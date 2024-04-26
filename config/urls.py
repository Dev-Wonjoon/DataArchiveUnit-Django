from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('downloader/', include('downloader.urls', namespace='downloader')),
    path('media/', include('album.urls', namespace='album'))
]
