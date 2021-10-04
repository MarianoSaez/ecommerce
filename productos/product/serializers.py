from rest_framework import serializers
from .models import Producto, Distribuidor


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'distribuidor',
            'cantidadVendido',
        ]


class DistribuidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribuidor
        fields = [
            'id',
            'nombre',
            'descripcion',
        ]
