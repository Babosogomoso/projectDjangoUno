from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

import tienda
from .models import Persona
from .forms import PersonaForm




def inicio(request):
    return HttpResponse("<h1>Bienvenido</h1>")

def index(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('///////////////////////////////////')
        return redirect('index')

    url = 'https://randomuser.me/api/?inc=name'
    data = requests.get(url)
    if data.status_code == 200:
        for e in data.json().get('results',[]):
            dt = e['name']
            first = dt['first']
            last = dt['last']
    return render(request,'index.html',{'first':first,'last':last})



   
