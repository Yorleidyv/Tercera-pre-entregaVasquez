from django import forms

class CrearPantoneFormulario(forms.Form):
    
    color = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)
    tono = forms.IntegerField()
    
class BusquedaPantoneFormulario (forms.Form):
    
    color = forms.CharField(max_length=30, required=False)
