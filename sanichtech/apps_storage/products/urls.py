from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('', products_list, name='show_products_list'),
    path('<int:id>', current_product, name='current_product'),

]
