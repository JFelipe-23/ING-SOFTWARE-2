from django import forms
from .models import Empleado

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['cedula', 'email', 'first_name', 'last_name', 'password']