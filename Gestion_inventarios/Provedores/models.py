from django.db import models
from Gestion_inventarios import Product

class Proovedor (models.Model):
    Nombre=models.CharField(max_length=150)
    Direccion=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=50)
    ID=models.IntegerField(max_length=10)
    Productos= models.ForeignKey(Product)

    def __str__(self):
        return f"Proveedor: {self.nombre}\n
        Dirección: {self.direccion}\n
        Teléfono: {self.telefono}\n
        Productos: {self.productos}"
    
    def __str__(self):
        return f"Productos: {self.Productos}"

    def agregar_producto(self, Productos):
        self.productos.append(Productos)

    def quitar_producto(self,Producto):
        if Producto in self.Productos:
            self.Productos.remove(Producto)
