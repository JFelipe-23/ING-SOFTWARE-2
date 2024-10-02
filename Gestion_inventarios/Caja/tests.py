from django.test import TestCase
from .models import Product

class productTest(TestCase):
    def setUp(self):
        # Crear algunos productos de prueba
        self.producto1 = Product.objects.create(
            codigo=200,
            nombre='Producto 1',
            precio=10.0,
            Provedor='Provedor A',
            descuento=0.1
        )
        self.producto2 = Product.objects.create(
            codigo=2,
            nombre='Producto 2',
            precio=10,
            Provedor='Provedor B',
            descuento=0
        )
        self.producto2 = Product.objects.create(
            codigo=-2,
            nombre='Producto 2',
            precio=500,
            Provedor='Provedor B',
            descuento=0.01
        )

    def test_crear_producto(self):
        """Asegura que se puedan crear productos correctamente."""
        self.assertEqual(Product.objects.count(), 3)

    def test_campos_producto(self):
        """Verifica los valores de los campos de un producto."""
        self.assertEqual(self.producto1.codigo, 200)
        self.assertEqual(self.producto1.nombre, 'Producto 1')
        self.assertEqual(self.producto1.precio, 10.0)
        self.assertEqual(self.producto1.Provedor, 'Provedor A')
        self.assertEqual(self.producto1.descuento, 0.1)

    def Test_metodos(self):
        producto1 = Product.objects.create(
                codigo=200,
                nombre='Producto 1',
                precio=10.0,
                Provedor='Provedor A',
                descuento=0.1
            )
        Product.agregar_descuento(producto1,0.5)

        Product.aplicar_descuento(producto1)