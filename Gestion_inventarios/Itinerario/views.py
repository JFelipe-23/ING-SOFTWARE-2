from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/logIn/")
def Itinerario(request):
    return render(request,'Itinerario.html')