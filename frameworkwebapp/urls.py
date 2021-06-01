
from django.urls import path
from frameworkwebapp import views

urlpatterns = [
path('',views.home, name=("home")),
path('tienda',views.tienda, name=("tienda")),
path('venta',views.venta, name=("venta")),
]