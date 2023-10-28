from django.urls import path
from inicio.views import inicio, pantones

urlpatterns = [
    path('', inicio),
    path('pantones/', pantones),
    ]
