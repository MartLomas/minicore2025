from django import forms
from django.forms import ModelForm
from .models import Vendedor, Venta, Reglas

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre']


class ReglaForm(forms.ModelForm):
    class Meta:
        model = Reglas
        fields = ['nombre', 'monto_min', 'monto_max', 'porcentaje']

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['vendedor', 'fecha', 'monto']