from django.db import models

class Pantone (models.Model):
    color = models.CharField(max_length=30)
    descripcion = models.TextField()
    tono = models.IntegerField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pantone = models.ForeignKey(Pantone, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=50, default='Pendiente')
    
    def __str__(self):
        return f'{self.id} - {self.pantone.color} - {self.pantone.tono}'


