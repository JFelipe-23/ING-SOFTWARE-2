from django.db import models

# Create your models here.

class User:
    def __init__(self,  usuario, Contraseña):
        self.usuario = usuario
        self.contraseña = Contraseña

#--------------------------------------------------------------------------
    def autenticar(self, usuario, contraseña):
        if self.usuario == usuario and self.contraseña == contraseña:
            return "Autenticación exitosa"
        else:
            return "Usuario o contraseña incorrectos"
#----------------------------------------------------------------------------  
    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
#----------------------------------------------------------------------------
    def cambiar_usuario(self, nuevo_usuario):
        """Actualiza el nombre de usuario."""
        self.usuario = nuevo_usuario
