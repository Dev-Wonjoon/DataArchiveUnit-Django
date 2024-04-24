import uuid
from datetime import datetime


def upload_to_rename(instance, filename):
    ext = filename.split('.')[-1]

    now = datetime.now()

    year = now.strftime('%Y')
    month = now.strftime('%m')
    day = now.strftime('%d')

    new_filename = f'{uuid.uuid4()}.{ext}'
    
    instance.extension = ext

    return f'uploads/{year}/{month}/{day}/{new_filename}'