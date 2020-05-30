from django import forms
from .models import *


class BebidasForm(forms.ModelForm):
    class Meta:
        model = Bebidas
        fields = ('type', 'price', 'status', 'issues')


class AlimentosForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = ('type', 'price', 'status', 'issues')


class AccesoriosForm(forms.ModelForm):
    class Meta:
        model = Accesorios
        fields = ('type', 'price', 'status', 'issues')


class LimpiezaForm(forms.ModelForm):
    class Meta:
        model = Limpieza
        fields = ('type', 'price', 'status', 'issues')
