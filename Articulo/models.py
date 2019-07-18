from django.db import models

# Create your models here.

TYPE_CHOICES = (
        ('PA','papa'),
        ('VR','verdura'),
        ('ET','etcetera'),
)

class Articulo(models.Model):
    descripcion = models.CharField(max_length=255,verbose_name='Descripcion') #descripcion del producto
    type = models.CharField(max_length=255,verbose_name='tipo_producto',choices=TYPE_CHOICES) #nombre de articulo
    Precio = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='precio venta') #precio actual
    Precio_Anterior = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='precio anterior') #precio anterior
    count_stock = models.IntegerField(default=0,verbose_name='existencia') #cantidad de articulos
    f_ingreso = models.DateTimeField(auto_now_add=True) #fecha en la que ingresa
    #id_proveedor = 
    #cod_almacen =
    def __unicode__(self):
        return self.descripcion
