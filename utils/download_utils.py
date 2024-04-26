import yt_dlp, os
from datetime import datetime

class YoutubeDownloader:
    def __init__(self, video_url):
        self.video_url = video_url

    def download_youtube(self):
        today = datetime.now().strftime("%Y/%m/%d")
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'media/{today}%{title}s%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(self.video_url, download=True)
            video_title = info_dict.get('title', 'unknown_title')
            filename = ydl.prepare_filename(info_dict)
        return filename, video_title
    
    @staticmethod
    def get_extension(filename):
        file_extension = os.path.splitext(filename)
        return file_extension
    

def printDate():
    today = datetime.now().strftime("%Y/%m/%d")
    print(today)

printDate()