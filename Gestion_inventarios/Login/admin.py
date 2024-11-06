from django.contrib import admin
from .models import Empleado

# Personalización de la visualización en el admin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'email', 'first_name', 'last_name', 'cumpleanos')
    search_fields = ('cedula', 'email', 'first_name', 'last_name')
    list_filter = ('cumpleanos',)

# Registrando el modelo Empleado en el admin
admin.site.register(Empleado, EmpleadoAdmin)