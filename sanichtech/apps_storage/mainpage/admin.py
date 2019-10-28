from django.contrib import admin

from .models import MainPage
from .models import MainPhotos

admin.site.register(MainPage)  # добавили все для нем
admin.site.register(MainPhotos)
