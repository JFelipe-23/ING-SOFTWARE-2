from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def Inicio(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'log_In.html')
    return render(request,'inicio.html')