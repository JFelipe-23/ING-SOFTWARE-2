from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre', 'precio', 'Provedor', 'descuento')
    list_filter = ('Provedor',)

admin.site.register(Product, ProductAdmin)