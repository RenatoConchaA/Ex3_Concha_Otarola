from django.contrib import admin
from .models import Producto, Descripcion

# Register your models here.

admin.site.register(Producto)
admin.site.register(Descripcion)