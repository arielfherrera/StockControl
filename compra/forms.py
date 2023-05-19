from django import forms
from .models import Proveedor, Producto

class ProveedorFormulario(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"

class ProductoFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"