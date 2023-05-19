from django.contrib import admin

# Register your models here.
from .models import Proveedor
from .models import Producto

admin.site.register(Proveedor)
admin.site.register(Producto)