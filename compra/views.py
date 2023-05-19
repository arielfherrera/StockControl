from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Proveedor, Producto
from .forms import ProveedorFormulario, ProductoFormulario

# Create your views here.

def proveedores(request):
    proveedores = Proveedor.objects.all()
    contexto = {
        'proveedores' : proveedores
    }
    return render(request,'proveedores.jinja', context=contexto)

def productos(request):
    productos = Producto.objects.all()
    contexto = {
        'productos' : productos
    }
    return render(request,'productos.jinja', context=contexto)

def agregar_proveedor(request):
    formulario = ProveedorFormulario()
    if request.method == 'POST':
        formulario = ProveedorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_proveedor/')
    contexto = {
        'formulario' : formulario
    }
    return render(request, 'agregar_proveedor.jinja', context=contexto)

def agregar_producto(request):
    formulario = ProductoFormulario()
    if request.method == 'POST':
        formulario = ProductoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            return HttpResponseRedirect('/agregar_producto/')
    contexto = {
        'formulario' : formulario
    }
    return render(request, 'agregar_producto.jinja', context=contexto)