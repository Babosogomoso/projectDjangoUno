from django.urls import path
from . import views

urlpatterns = [
     path('', views.inicio, name='inicio'),
     path('home', views.home, name='home'),
     path('api', views.api, name='api'),
     path('servicio', views.servicios, name='Servicios'),
     path('producto', views.productos, name='Productos'),
     path('reserva', views.reserva, name='Reserva'),
     path('galeria', views.galeria, name='Galeria'),
]