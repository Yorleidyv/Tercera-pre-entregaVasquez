from django.shortcuts import render, redirect

from inicio.models import Pantone, Cliente, Pedido

from inicio.forms import CrearPantoneFormulario, BusquedaPantoneFormulario, CrearClienteFormulario, CrearPedidoFormulario, BusquedaClienteFormulario, BusquedaPedidoFormulario

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

def clientes(request):
    formulario = BusquedaClienteFormulario(request.GET)
    listado_de_clientes = Cliente.objects.all()
    
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        email = formulario.cleaned_data.get('email')
        direccion = formulario.cleaned_data.get('direccion')
        
        if nombre:
            listado_de_clientes = listado_de_clientes.filter(nombre__icontains=nombre)
        if email:
            listado_de_clientes = listado_de_clientes.filter(email__icontains=email)
        if direccion:
            listado_de_clientes = listado_de_clientes.filter(direccion__icontains=direccion)
    
    formulario = BusquedaClienteFormulario()
    return render(request, 'inicio/clientes.html', {'formulario': formulario, 'listado_de_clientes': listado_de_clientes})

def crear_cliente(request):
    if request.method == 'POST':
        formulario = CrearClienteFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes')
    else:
        formulario = CrearClienteFormulario()
    return render(request, 'inicio/crear_cliente.html', {'formulario': formulario})

def pedidos(request):
    formulario = BusquedaPedidoFormulario(request.GET)
    listado_de_pedidos = Pedido.objects.all()
    
    if formulario.is_valid():
        cliente = formulario.cleaned_data.get('cliente')
        pantone = formulario.cleaned_data.get('pantone')
        cantidad = formulario.cleaned_data.get('cantidad')
        fecha_pedido = formulario.cleaned_data.get('fecha_pedido')
        estado = formulario.cleaned_data.get('estado')
        
        if cliente:
            listado_de_pedidos = listado_de_pedidos.filter(cliente=cliente)
        if pantone:
            listado_de_pedidos = listado_de_pedidos.filter(pantone=pantone)
        if cantidad:
            listado_de_pedidos = listado_de_pedidos.filter(cantidad=cantidad)
        if fecha_pedido:
            listado_de_pedidos = listado_de_pedidos.filter(fecha_pedido=fecha_pedido)
        if estado:
            listado_de_pedidos = listado_de_pedidos.filter(estado__icontains=estado)
    
    formulario = BusquedaPedidoFormulario()
    return render(request, 'inicio/pedidos.html', {'formulario': formulario, 'listado_de_pedidos': listado_de_pedidos})

def crear_pedido(request):
    if request.method == 'POST':
        formulario = CrearPedidoFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('pedidos')
    else:
        formulario = CrearPedidoFormulario()
    return render(request, 'inicio/crear_pedido.html', {'formulario': formulario})
    
