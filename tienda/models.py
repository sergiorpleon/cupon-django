from django.db import models
from django.contrib.auth.models import User
from django.db import models
from ciudad.models import *

# Create your models here.
class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    direccion = models.CharField(max_length=500)
    ciudad = models.ForeignKey(Ciudad)
    propietario = models.ForeignKey(User)

    def __str__(self):
        return self.nombre