from django.test import TestCase
from .models import User
# Create your tests here.

class Login_tests(TestCase):
    def setUp(self):
        self.user = User("Juan18", "contraseña18")

    def test_autenticacion_exitosa(self):
        resultado = self.user.autenticar("Juan18", "contraseña18")
        self.assertEqual(resultado, "Autenticación exitosa")
#--------------------------------------------------------------------------------------
#    def test_autenticacion_fallida(self):}

#---------------------------------------------------------------------------------------
    def test_cambiar_contraseña(self):

        self.user.cambiar_contraseña("David18")
        resultado = self.user.autenticar("Juan18", "David18")
        self.assertEqual(resultado, "Autenticación exitosa")
#---------------------------------------------------------------------------------------
    def test_cambiar_usuario(self):
        # Cambiar usuario y verificar autenticación
        self.user.cambiar_usuario("David18")
        resultado = self.user.autenticar("David18", "contraseña18")
        self.assertEqual(resultado, "Autenticación exitosa")


