from django.db import models

# Create your models here.
class Almacen(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=12)
    direccion=models.TextField()