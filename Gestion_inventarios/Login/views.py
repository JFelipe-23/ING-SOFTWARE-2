from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from Login.form import VendedorForm  # Asegúrate de que este formulario exista

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('/')  # Reemplaza 'home' con la URL de tu página principal
    else:
        form = AuthenticationForm()
    return render(request, 'log_In.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = VendedorForm()
    return render(request, 'register.html', {'form': form})