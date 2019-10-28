from django.contrib import admin

from .models import Service
from .models import AddFiles

admin.site.register(Service)
admin.site.register(AddFiles)

