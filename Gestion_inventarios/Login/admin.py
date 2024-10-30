from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empleado

class VendedorAdmin(UserAdmin):
    list_display = ( 'email', 'first_name', 'last_name', 'cedula')
    search_fields = ( 'email', 'first_name', 'last_name', 'cedula')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'cedula')}),
    )

admin.site.register(Empleado, VendedorAdmin)