from django.urls import path
from .views import *

app_name = 'services'
urlpatterns = [
    path('', services_list, name='show_services_list'),
    path('<int:id>', current_service, name='current_service'),

]
