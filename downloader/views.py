import logging

from django.views import View
from django.shortcuts import render
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
        
        check_url = Url.objects.filter(link=video_url)

        if not check_url:
            downloader = YoutubeDownloader(video_url)
            filename, video_title = downloader.download_youtube()
        elif check_url:
            error_message = '중복된 url이 있습니다.'
            logging.error(error_message)
            return render(request, self.template_name, {'error': error_message})
        
        if filename is None:
            error_message = '비디오 처리 중 오류가 발생했습니다.'
            logging.error(error_message)
            return render(request, self.template_name, {'error': error_message})
            
        try:
            logging.info(f"{video_url} downloading")
            file_path = upload_to_rename(None, filename)
            file_extension = filename.split('.')[-1].lower()
            media_item = MediaItem(path=file_path, extension=file_extension)
            media_item.save()
            url_item = Url(title=video_title, link=video_url, site='Youtube', media=media_item)
            url_item.save()

            return render(request, 'downloader/download_form.html', {'message': '비디오 다운로드가 완료 되었습니다.'})
            
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            return render(request, self.template_name, {'error': '비디오 처리 중 오류가 발생했습니다.'})