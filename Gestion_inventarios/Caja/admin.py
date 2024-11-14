from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id','fecha', 'total_pedido', 'vendedor', 'get_productos')
    list_filter = ('fecha', 'vendedor')
    search_fields = ('id', 'vendedor__username')
    readonly_fields = ('fecha',)

    def get_productos(self, obj):
        return ", ".join([p.nombre for p in obj.productos.all()])
    
    get_productos.short_description = 'Productos'

admin.site.register(Pedido, PedidoAdmin)

