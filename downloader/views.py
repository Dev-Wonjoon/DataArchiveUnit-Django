from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from album.models import MediaItem
from downloader.models import Url
from utils.download_utils import YoutubeDownloader
from utils.uuid_utils import upload_to_rename


class YoutubeDownloadView(View):
    template_name = 'downloader/download_form.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        video_url = request.POST.get('url', '')
        downloader = YoutubeDownloader(video_url)
        filename, video_title = downloader.download_youtube()
        file_extension = downloader.get_extension(filename)

        file_path = upload_to_rename(None, filename)

        media_item = MediaItem(path=file_path, extension=file_extension)
        media_item.save()

        url_item = Url(title=video_title, link=video_url, site='Youtube')
        url_item.save()

        return render(request, 'downloader')