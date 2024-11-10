from django.db import models
from Login.models import Empleado
from Provedores.models import Proveedor


class Producto(models.Model):
    isbn = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        if self.descuento==0:
            self.precio_final=self.precio_base
        else:
            self.precio_final = self.precio_base-((self.precio_base * self.descuento) / 1)
        super(Producto, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.nombre}"

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto)
    vendedor = models.ForeignKey(Empleado, on_delete=models.CASCADE)