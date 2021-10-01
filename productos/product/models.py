from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey


class Distribuidor(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=280)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=280)
    precio = models.FloatField()
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    cantidadVendido = models.IntegerField()

    def __str__(self):
        return str(self.nombre)


    