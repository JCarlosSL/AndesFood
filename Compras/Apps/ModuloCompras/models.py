from django.db import models
from Apps.ModuloAlmacen.models import Almacen
# Create your models here.
class Provehedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    sexo=models.CharField( max_length=10)
    edad=models.IntegerField()
    telefono=models.CharField(max_length=12)
    email=models.EmailField(max_length=254)
    domicilio=models.TextField()
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=19, decimal_places=10)
class Producto_Almacen(models.Model):
    producto=models.ForeignKey(Producto,null=True,blank=True, on_delete=models.CASCADE)
    almacen=models.ForeignKey(Almacen,null=True,blank=True, on_delete=models.CASCADE)
    cantidadProductos=models.IntegerField()
class Compra(models.Model):
    fechaCompra=models.DateField()
    CostoTotal=models.DecimalField(max_digits=50, decimal_places=20)
    provehedor=models.ForeignKey(Provehedor,null=True,blank=True, on_delete=models.CASCADE)    
class Compra_Producto(models.Model):
    compra=models.ForeignKey(Compra,null=True,blank=True, on_delete=models.CASCADE)    
    producto=models.ForeignKey(Producto,null=True,blank=True, on_delete=models.CASCADE)    
    cantidadProductos=models.IntegerField()
        
