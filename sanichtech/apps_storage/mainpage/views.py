from django.shortcuts import render, redirect
from .models import *
from django.http.response import Http404


def default_lang(request):
    return redirect('mainpage:show_mainpage', 'ru')


def change_lang(request, ch_lang):
    return redirect('mainpage:show_mainpage', ch_lang)


def bmain(request, cur_lang):
    return redirect('mainpage:show_mainpage', cur_lang)


def show_mainpage(request, lang):
    if lang in ['ru', 'ukr', 'en', 'de']:
        aboutus = MainPage.objects.all()  # взли КС главной страницы укр (КвериСет)
        response_dict = {'lang': lang, 'aboutus': aboutus, }
        return render(request, 'main_page.html', response_dict)
    else:
        raise Http404('No language!')


def prod_or_serv(request, lang, ps):
    if lang in ['ru', 'ukr', 'en', 'de'] and ps in ['products', 'services']:
        return redirect('/'+lang+'/'+ps+'/', permanent=True)
    else:
        raise Http404('No language or section!')


