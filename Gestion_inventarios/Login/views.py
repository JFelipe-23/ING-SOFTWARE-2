from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

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