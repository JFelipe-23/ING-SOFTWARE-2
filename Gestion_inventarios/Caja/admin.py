from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('codigo_Producto','nombre', 'precio', 'codigo_Provedor', 'descuento')
    list_filter = ('codigo_Provedor',)

admin.site.register(Product, ProductAdmin)