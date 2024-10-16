from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=10)

# Metodos
#-----------------------------------------------------------------------------------
    def __str__(self):
        return f"Usuario: {self.usuario}"
#-----------------------------------------------------------------------------------
    def autenticar(self, usuario, contraseña):
        if self.usuario == usuario and self.contraseña == contraseña:
            return "Autenticación exitosa"
        else:
            return "Usuario o contraseña incorrectos"
#-----------------------------------------------------------------------------------
    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
        self.save()
#-----------------------------------------------------------------------------------
    def cambiar_usuario(self, nuevo_usuario):
        self.usuario = nuevo_usuario
        self.save()






