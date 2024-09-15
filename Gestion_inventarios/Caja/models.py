from django.db import models

class Product(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    Provedor = models.CharField(max_length=100)
    descuento = models.FloatField()