from django.contrib import admin

from .models import Product
from .models import AddFiles

admin.site.register(Product)  # добавили все для нем
admin.site.register(AddFiles)
