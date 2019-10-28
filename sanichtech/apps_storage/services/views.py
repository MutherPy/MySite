from django.shortcuts import render
from .models import *
from django.http.response import Http404


def services_list(request, lang):
    if lang in ['ru', 'ukr', 'en', 'de']:
        try:
            services = Service.objects.all()
        except:
            raise Http404()
        response_dict = {'lang': lang, 'services': services, 'what': 'serv', }
        return render(request, 'list.html', response_dict)
    else:
        raise Http404('Incorrect lang!!')


def current_service(request, lang, id):
    if lang in ['ru', 'ukr', 'en', 'de']:
        try:
            choosed_service = Service.objects.get(id=id)
        except:
            raise Http404('No service!')
        response_dict = {'lang': lang, 'choosed_service': choosed_service, 'what': 'serv', }
        return render(request, 'current_choose.html', response_dict)
    else:
        raise Http404('No lang!')
