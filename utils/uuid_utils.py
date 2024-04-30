import uuid
from datetime import datetime


def upload_to_rename(instance, filename):
    ext = filename.split('.')[-1].lower()

    now = datetime.now()

    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')

    new_filename = f'{uuid.uuid4()}.{ext}'
    
    if instance is not None:
        instance.extension = ext

    return f'media/{year}/{month}/{day}/{new_filename}'

def video_to_rename():
    return uuid.uuid4()