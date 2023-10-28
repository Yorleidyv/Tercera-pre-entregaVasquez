from django.shortcuts import render

from inicio.models import Pantone

def inicio (request):
    
    return render (request, 'inicio/inicio.html', {})

def pantones (request):
    
    pantone = Pantone(color='azul', descripcion='azul oscuro', tono=23)
    pantone.save()
    
    return render (request, 'inicio/pantones.html', {'pantone': pantone})
    

# Create your views here.
