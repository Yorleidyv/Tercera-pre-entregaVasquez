from django.shortcuts import render, redirect

from inicio.models import Pantone

from inicio.forms import CrearPantoneFormulario, BusquedaPantoneFormulario

def inicio (request):
    
    return render (request, 'inicio/inicio.html', {})

def pantones(request):
    
    #v1
    # color_a_buscar = request.GET.get('color')
    
    # if color_a_buscar:
    #     listado_de_pantones = Pantone.objects.filter(color__icontains=color_a_buscar)
    # else:
    #     listado_de_pantones = Pantone.objects.all()
    #v1
    
    formulario = BusquedaPantoneFormulario(request.GET)
    if formulario.is_valid():
        color_a_buscar = formulario.cleaned_data.get('color')
        listado_de_pantones = Pantone.objects.filter(color__icontains=color_a_buscar)
        
    formulario = BusquedaPantoneFormulario()
    return render(request, 'inicio/pantones.html', {'formulario': formulario, 'listado_de_pantones': listado_de_pantones})

def crear_pantone(request):
    
    if request.method == 'POST':
        formulario = CrearPantoneFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            color = info_limpia.get('color')
            descripcion = info_limpia.get('descripcion')
            tono = info_limpia.get('tono')
            
            pantone = Pantone(color=color.lower(), descripcion=descripcion, tono=tono)
            pantone.save()
            
            return redirect('pantones')  
        else:
            return render(request, 'inicio/crear_pantone.html', {'formulario' : formulario})
    
    formulario = CrearPantoneFormulario()
    return render(request, 'inicio/crear_pantone.html', {'formulario': formulario})
    
