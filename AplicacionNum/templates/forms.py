from django import forms
from django.forms import ModelForm
from AplicacionNum.models import Producto


class ProductForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombrepro', 'descripcionpro', 'imagenpro','stock','categoria']