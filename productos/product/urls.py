from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProductoView.as_view()),
    path('vendido/', views.ProductoVendidoView.as_view())
]
