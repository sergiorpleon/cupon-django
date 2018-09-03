from django.db import models
from django.contrib.auth.models import User
from django.db import models
from ciudad.models import *
from tienda.models import *

# Create your models here.
class Oferta(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    condiciones = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, )
    precio = models.DecimalField(max_digits  = 5, decimal_places = 2)
    descuento = models.DecimalField(max_digits  = 5, decimal_places = 2)
    fecha_expiracion = models.DateField(blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    compra = models.IntegerField()
    umbral = models.IntegerField()
    revisada = models.IntegerField()
    ciudad = models.ForeignKey(Ciudad)
    tienda = models.ForeignKey(Tienda)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateField(blank=True, null=True)
    oferta = models.ForeignKey(Oferta)
    usuario = models.ForeignKey(User)

    def __str__(self):
        return "%s - %s" % (self.oferta.nombre, self.usuario.username)