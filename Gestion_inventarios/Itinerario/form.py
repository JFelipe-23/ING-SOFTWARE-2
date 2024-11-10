from django import forms
from Caja.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['isbn' ,'nombre','cantidad', 'precio_base', 'descuento', 'proveedor']

class EditarProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['cantidad', 'precio_base', 'descuento']