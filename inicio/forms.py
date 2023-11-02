from django import forms
from .models import Cliente, Pedido, Pantone

class CrearPantoneFormulario(forms.Form):
    
    color = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)
    tono = forms.IntegerField()
    
class BusquedaPantoneFormulario (forms.Form):
    
    color = forms.CharField(max_length=30, required=False)

class CrearClienteFormulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CrearPedidoFormulario(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class BusquedaClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False)
    direccion = forms.CharField(max_length=200, required=False)

class BusquedaPedidoFormulario(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False)
    pantone = forms.ModelChoiceField(queryset=Pantone.objects.all(), required=False)
    cantidad = forms.IntegerField(required=False)
    fecha_pedido = forms.DateField(required=False)
    estado = forms.CharField(max_length=50, required=False)
