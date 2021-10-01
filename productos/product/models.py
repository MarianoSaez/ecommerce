from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=280)
    precio = models.FloatField()
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    cantidadVendido = models.IntegerField()

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=280)
    