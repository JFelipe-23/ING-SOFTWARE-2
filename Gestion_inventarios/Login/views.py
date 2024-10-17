from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'inicio.html')
    else:
        messages.error(request, 'Credenciales inválidas.')
    return render(request, 'log_In.html')