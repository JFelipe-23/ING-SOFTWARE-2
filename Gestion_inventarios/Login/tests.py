from django.test import TestCase
from models import User
# Create your tests here.



class UserModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(usuario="David17", contraseña="123456789")

    def test_autenticacion_exitosa(self):
        resultado = self.user.autenticar("David17", "123456789")
        self.assertEqual(resultado, "Autenticación exitosa")
#--------------------------------------------------------------------------------------------------
    def test_autenticacion_fallida(self):
        resultado = self.user.autenticar("David17", "13456789")
        self.assertEqual(resultado, "Usuario o contraseña incorrectos")
#--------------------------------------------------------------------------------------------------
    def test_cambiar_contraseña(self):
        self.user.cambiar_contraseña("987654321")
        self.user.refresh_from_db() 
        self.assertEqual(self.user.contraseña, "987654321")

        resultado = self.user.autenticar("Pato", "987654321")
        self.assertEqual(resultado, "Autenticación exitosa")
#--------------------------------------------------------------------------------------------------
    def test_cambiar_usuario(self):
        self.user.cambiar_usuario("David18")
        self.user.refresh_from_db()
        self.assertEqual(self.user.usuario, "David18")
      
        resultado = self.user.autenticar("David18", "987654321")
        self.assertEqual(resultado, "Autenticación exitosa")

