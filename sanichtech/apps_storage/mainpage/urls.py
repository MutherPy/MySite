from django.urls import path
from .views import *

app_name = 'mainpage'
urlpatterns = [
    path('', default_lang, name='default_lang'),
    path('<str:lang>/', show_mainpage, name='show_mainpage'),
    path('<str:ch_lang>/chlang/', change_lang, name='change_lang'),
    path('<str:cur_lang>/main/', bmain, name='back_to_main'),
    path('<str:lang>/<str:ps>', prod_or_serv, name='show_prod_or_serv'),

]
