
from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    template = loader.get_template('frameworkwebapp/home.html')
    context = {

    }
    return HttpResponse(template.render(context, request))

def tienda(request):
    template = loader.get_template('frameworkwebapp/tienda.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def venta(request):
    template = loader.get_template('frameworkwebapp/venta.html')
    context = {

    }
    return HttpResponse(template.render(context, request))