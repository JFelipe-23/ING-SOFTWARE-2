from django.db import models

class Proveedor(models.Model):
    nit = models.CharField(max_length=20, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self) -> str:
        return f"{self.nombre}"