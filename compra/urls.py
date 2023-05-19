from django.urls import path
from . import views

urlpatterns = [
    path("proveedores/", views.proveedores, name="vistaProveedores"),
    path("productos/", views.productos, name="vistaProductos"),
    path("proveedores/agregar_proveedor/", views.agregar_proveedor, name="vistaAgregar_Proveedor"),
    path("productos/agregar_producto/", views.agregar_producto, name="vistaAgregar_Producto"),
]