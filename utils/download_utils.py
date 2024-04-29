import yt_dlp, os
from datetime import datetime

class YoutubeDownloader:
    def __init__(self, video_url):
        self.video_url = video_url

    def download_youtube(self):
        try:
            today = self.get_today_date()
            ydl_opts = {
                'default_search': 'ytsearch',
                'format': 'bestvideo+bestaudio',
                'outtmpl': f'F:/dau/media/{today}%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.video_url, download=True)
                video_title = info_dict.get('title', 'unknown_title')
                filename = ydl.prepare_filename(info_dict)
            return filename, video_title
        except Exception as e:
            print(f"Error downloading video: {e}")
            return None, None
    
    @staticmethod
    def get_extension(filename):
        file_extension = os.path.splitext(filename)
        return file_extension[1:]
    
    @staticmethod
    def get_today_date():
        return datetime.now().strftime(f"%Y/%m/%d/")