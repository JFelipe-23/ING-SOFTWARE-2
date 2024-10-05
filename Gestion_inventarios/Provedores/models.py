from django.db import models
from Gestion_inventarios import Caja

class Proovedor:
    def __init__(self, Nombre, direccion, telefono, ID,):
        self.Nombre=Nombre
        self.Direccion=direccion
        self.telefono=telefono
        self.ID=ID
        self.Productos=[]

    def __str__(self):
        return f"Proveedor: {self.nombre}\n
        Dirección: {self.direccion}\n
        Teléfono: {self.telefono}\n
        Productos: {self.productos}"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def quitar_producto(self,producto):
        if producto in self.Productos:
            self.Productos.remove(producto)
