from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

def login(request):
    return render(request,'log_In.html')

def Itinerario(request):
    return render(request,'Itinerario.html')

def Caja(request):
    return render(request,'caja.html')

def Calendario(request):
    return render(request,'calendario.html')

def Inicio(request):
    return render(request,'inicio.html')

def Provedores(request):
    return render(request,'provedor.html')