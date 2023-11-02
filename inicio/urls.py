from django.urls import path
from inicio.views import inicio, pantones, crear_pantone, clientes, crear_cliente, pedidos, crear_pedido

urlpatterns = [
    path('', inicio, name='inicio'),
    path('pantones/', pantones, name='pantones'),
    path('pantones/crear/', crear_pantone, name='crear_pantone'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente'),
    path('pedidos/', pedidos, name='pedidos'),
    path('pedidos/crear/', crear_pedido, name='crear_pedido'),
    ]
