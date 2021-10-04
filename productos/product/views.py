from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import ProductoSerializer, DistribuidorSerializer
from .models import Producto


# Create your views here.

# Esta vista solo implementa el metodo GET dado
# que solo requiere devolver un listado de los productos
# disponibles
class ProductoView(generics.ListAPIView):
    model = Producto
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


# Se recibe la lista de ventas completa y se actualizan
# en tanda todos los productos vendidos
# 
# Carro de compras ->
# {
#   "85" : 3,
#   "63" : 1,
#   "10" : 20, 
# }
# -> Producto


class ProductoVendidoView(generics.GenericAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        listaProductos = [i for i in self.request.data.keys()]
        # https://docs.djangoproject.com/en/3.2/topics/db/queries/#the-pk-lookup-shortcut
        return Producto.objects.filter(pk__in=listaProductos)

    def get_object(self):
        return self.get_queryset()

    def patch(self, request):
        productosVendidos = self.get_object()
        updateDict = self.request.data
        for producto in productosVendidos:
            data = {
                "cantidadVendido" : updateDict[str(producto.pk)] + producto.cantidadVendido
            }
            serializer = ProductoSerializer(producto, data=data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=500)
        return Response(serializer.data, status=200)
