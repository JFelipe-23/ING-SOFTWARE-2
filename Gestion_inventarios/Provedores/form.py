from django import forms
from .models import Proveedor

class ProvedorFormulario(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

class EditarProvedorFormulario(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['correo','telefono','direccion']