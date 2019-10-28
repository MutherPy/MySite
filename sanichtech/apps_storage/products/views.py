from django.shortcuts import render
from .models import *
from django.http.response import Http404


def products_list(request, lang):
    if lang in ['ru', 'ukr', 'en', 'de']:
        try:
            products = Product.objects.all()
        except:
            raise Http404()
        response_dict = {'lang': lang, 'products': products, 'what': 'prod', }
        return render(request, 'list.html', response_dict)
    else:
        raise Http404('Incorrect lang!')


def current_product(request, lang, id):
    if lang in ['ru', 'ukr', 'en', 'de']:
        try:
            choosed_product = Product.objects.get(id=id)
        except:
            raise Http404('No product!')
        response_dict = {'lang': lang, 'choosed_product': choosed_product, 'what': 'prod', }
        return render(request, 'current_choose.html', response_dict)
    else:
        raise Http404('No lang!')
