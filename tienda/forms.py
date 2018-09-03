from django import forms

class FormularioTienda(forms.Form):
    nombre = forms.CharField(max_length=100)
    slug = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=500, widget=forms.Textarea)
    direccion = forms.CharField(max_length=500, widget=forms.Textarea)
    
    # ciudad = forms.ForeignKey(Ciudad)
    # tienda = forms.ForeignKey(Tienda)