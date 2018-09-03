from django import forms
from oferta.models import *
from django.forms import ModelForm

class FormularioOferta(ModelForm):
    class Meta:
		model = Oferta
		exclude = ("ciudad","tienda",)
    # ciudad = forms.ForeignKey(Ciudad)
    # tienda = forms.ForeignKey(Tienda)
