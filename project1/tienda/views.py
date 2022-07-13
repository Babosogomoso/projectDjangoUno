from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .models import Persona
from .forms import PersonaForm
from django.conf import settings


def inicio(request):
    return render(request,'home.html')

def api(request):
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():   
            formulario.save()
            print(formulario)
            return HttpResponse('Guardado')

    url = 'https://randomuser.me/api/?inc=name'
    data = requests.get(url)
    if data.status_code == 200:
        for e in data.json().get('results',[]):
            dt = e['name']
            first = dt['first']
            last = dt['last']
    return render(request,'api.html',{'first':first,'last':last})


def servicios(request):
   return render(request,'servicios.html')

def reserva(request):
   return render(request,'reserva.html')

def productos(request):
   return render(request,'productos.html')

def galeria(request):
    return render(request,'galeria.html')

def home(request):
    return render(request,'home.html')

