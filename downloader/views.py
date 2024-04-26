import logging
from django.core.files import File

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from album.models import MediaItem
from downloader.models import Url
from utils.download_utils import YoutubeDownloader
from utils.uuid_utils import upload_to_rename


class YoutubeDownloadView(View):
    template_name = 'downloader/download_form.html'
    logging.basicConfig(level=logging.DEBUG)

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        video_url = request.POST.get('url', '').strip()
        logging.debug(f'URL: {video_url}')

        if not video_url:
            return render(request, self.template_name, {'error': 'URL을 입력해주세요'})
        
        downloader = YoutubeDownloader(video_url)
        filename, video_title = downloader.download_youtube()
        
        if filename is None:
            error_message = '비디오 다운로드에 실패했습니다.'
            logging.error(error_message)
            return render(request, self.template_name, {'error': error_message})
        
        try:
            file_path = upload_to_rename(None, filename)
            file_extension = filename.split('.')[-1].lower()

            media_item = MediaItem(path=file_path, extension=file_extension)
            media_item.save()

            url_item = Url(title=video_title, link=video_url, site='Youtube')
            url_item.save()

            return render(request, 'downloader/download_form.html', {'message': '비디오 다운로드가 완료 되었습니다.'})
        
        except Exception as e:
            logging.debug(f'file_extension')
            logging.error(f'An error occurred: {e}')
            return render(request, self.template_name, {'error': '비디오 처리 중 오류가 발생했습니다.'})