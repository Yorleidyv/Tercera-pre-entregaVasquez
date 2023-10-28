from django.db import models

class Pantone (models.Model):
    color = models.CharField(max_length=30)
    descripcion = models.TextField()
    tono = models.IntegerField()
# Create your models here.
