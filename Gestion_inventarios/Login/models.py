from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class EmpleadoManager(BaseUserManager):
    def create_user(self, cedula, email, first_name, last_name, password=None):
        """
        Creates and saves a new user.
        """
        if not cedula:
            raise ValueError('The cedula must be set')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            cedula=cedula,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cedula, email, first_name, last_name, password):
        """
        Creates and saves a new superuser.
        """
        user = self.create_user(
            cedula=cedula,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Empleado(AbstractUser):
    cedula = models.CharField(max_length=20, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cumpleanos = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    USERNAME_FIELD = 'cedula'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = EmpleadoManager()

    def __str__(self) -> str:
        return f"{self.cedula}"