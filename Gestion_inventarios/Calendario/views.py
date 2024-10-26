from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def Calendario(request):
    return render(request,'calendario.html')