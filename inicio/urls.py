from django.urls import path
from inicio.views import inicio, pantones, crear_pantone

urlpatterns = [
    path('', inicio, name='inicio'),
    path('pantones/', pantones, name='pantones'),
    path('pantones/crear/', crear_pantone, name='crear_pantone'),
    ]
