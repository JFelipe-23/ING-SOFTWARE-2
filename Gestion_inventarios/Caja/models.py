from django.db import models

class Product(models.Model):
    codigo_Producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    codigo_Provedor = models.IntegerField()
    descuento = models.FloatField()

    def _str_(self):
        return f"Producto: {self.nombre} ({self.codigo})"
    
    def aplicar_descuento(self):
        return self.precio*1-(self.descuento/100)
    
    def agregar_descuento(self, nuevo_descuento):
        self.descuento = nuevo_descuento
        self.save()