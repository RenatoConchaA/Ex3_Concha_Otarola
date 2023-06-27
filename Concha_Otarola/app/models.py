from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(db_column='idProducto', primary_key=True)
    producto = models.CharField(max_length=25, blank=False, null=False)
    descripcion = models.CharField(max_length=50)
    precio = models.CharField(max_length=7)
    activo = models.IntegerField()

    def __str__(self):
        return str(self.producto)+" "+ str(self.descripcion)+" "+str(self.precio)