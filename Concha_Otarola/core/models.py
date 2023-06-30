from django.db import models

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(max_length=25, blank=False, null=False)
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=7)