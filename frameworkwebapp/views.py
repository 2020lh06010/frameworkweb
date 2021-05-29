
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("home")

def tienda(request):
    return HttpResponse("tienda")

def venta(request):
    return HttpResponse("venta")