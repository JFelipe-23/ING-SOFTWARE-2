from django.db import models

# Create your models here.

# Caja
#class Caja(models.Model):
    

                            #TERMINAR
        
#-----------------------------------------------------------------------------------
# Inventario

class Inventario(models.Model):
    nombre_producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)    

    def __str__(self):
        return self.nombre_producto
#-----------------------------------------------------------------------------------
# poveedor

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    contacto = models.CharField(max_length=10)               #TERMINAR

    def __str__(self):
        return self.nombre
#-----------------------------------------------------------------------------------
# Calendario

class Calendario(models.Model):
    evento = models.CharField(max_length=200)                #TERMINAR

    