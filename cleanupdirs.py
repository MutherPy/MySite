import os
from sanichtech.settings import BASE_DIR

""" Скрипт чистит пустые папки в медии по продуктам и по проэктам """


def remove_empty_media_dirs():
    dirs_prod = os.listdir(path=os.path.join(BASE_DIR, r'media/media/photos/products/'))
    for dir_p in dirs_prod:
        try:
            os.rmdir(os.path.join(BASE_DIR, r'media/media/photos/products/{}').format(dir_p))
        except:
            pass

    dirs_serv = os.listdir(path=os.path.join(BASE_DIR, r'media/media/photos/services/'))
    for dir_s in dirs_serv:
        try:
            os.rmdir(os.path.join(BASE_DIR, r'media/media/photos/services/{}').format(dir_s))
        except:
            pass


remove_empty_media_dirs()
