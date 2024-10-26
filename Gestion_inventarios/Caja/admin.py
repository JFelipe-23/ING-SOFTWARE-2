from django.contrib import admin
from .models import Producto, Pedido, PedidoProducto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'nombre', 'cantidad', 'precio_base', 'precio_final', 'proveedor')
    list_filter = ('proveedor',)
    search_fields = ('isbn', 'nombre')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'total_del_pedido', 'medio_de_pago', 'vendedor')
    list_filter = ('fecha', 'medio_de_pago')
    search_fields = ('id', 'vendedor__user__email')

@admin.register(PedidoProducto)
class PedidoProductoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad')
    list_filter = ('pedido', 'producto')
