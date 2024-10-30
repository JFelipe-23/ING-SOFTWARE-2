from django.contrib import admin
from .models import Proveedor

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit', 'correo')
    search_fields = ('nombre', 'nit')

admin.site.register(Proveedor, ProveedorAdmin)