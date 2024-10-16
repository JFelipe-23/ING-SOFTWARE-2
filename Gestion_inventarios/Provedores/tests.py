from django.test import TestCase
from .models import Proovedor, Producto


# Create your tests here.
class ProveedorTestCase(TestCase):
    def setup(self):
        #Creacion de producto del proveedor
        self.Producto= Producto.objects.create(Nombre="Madera Plastica")

        #Creacion del proovedor
        self.Proovedor= Proovedor.objects.create(
            Nombre="Maderas ABS",
            Direccion="CALLE 75 N 41-20 BARRIO EL PARAISO LOS 2500 LOTES MZ 13 CASA 10",
            Telefono="3138457291",
            ID= 81
        )


        self.Proovedor.Productos.add(self.Producto)


        #Prueba Metodo __str__

        def Testeo_str(self):
            self.assertEqual(
                str(self.proveedor),
                "Proveedor: Maderas ABS\n"
                "Direccion:CALLE 75 N 41-20 BARRIO EL PARAISO LOS 2500 LOTES MZ 13 CASA 10\n"
                "Telefono: 3138457291\n"
                "Producto: Maderas Plasticas",
            )

        #Hacer conexion productos: Proveedor-Caja

        
        def Testeo_Agregacion(self):
            Nuevo_Pro= Producto.objects.create(Nombre="Madera de Roble")

            self.Proovedor.agregar_producto(Nuevo_Pro)
            self.assertIn(Nuevo_Pro, self.proveedor.productos.all())


        def Testeo_QuitarProducto(self):

            self.Proovedor.quitar_producto(self.producto)
            self.assertNotIn(self.producto,
                             self.proveedor.productos.all())
