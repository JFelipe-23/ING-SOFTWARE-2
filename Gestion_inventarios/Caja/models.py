from django.db import models
from Login.models import Vendedor, Proveedor

class Producto(models.Model):
    isbn = models.CharField(max_length=13, primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"Producto: {self.nombre} - {self.isbn}"

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    total_del_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    medio_de_pago = models.CharField(max_length=50)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, related_name='pedidos')
    productos = models.ManyToManyField(Producto, through='PedidoProducto')

    def __str__(self):
        return f"Pedido ID: {self.id} - {self.fecha}"

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Pedido {self.pedido.id} - Producto {self.producto.isbn}"
