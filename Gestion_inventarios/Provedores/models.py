from django.db import models

class Proovedor (models.Model):
    Nombre=models.CharField(max_length=150)
    Direccion=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=50)
    Codigo_Provedor=models.IntegerField(primary_key=True)

    def __str__(self):
        txt = ""
        txt += f"Proveedor: {self.nombre}\n"
        txt += f"Dirección: {self.direccion}\n"
        txt += f"Teléfono: {self.telefono}\n"
        txt += f"Productos: {self.productos}"
        return txt

    def agregar_producto(self, Productos):
        self.productos.append(Productos)

    def quitar_producto(self,Producto):
        if Producto in self.Productos:
            self.Productos.remove(Producto)
