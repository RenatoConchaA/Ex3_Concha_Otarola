from django.urls import path
from .views import index, about, gallery, formulario, API, register, agregar, agregarrec, eliminar,actualizar,actualizarrec

urlpatterns = [
    path('', index, name='index'),
    path('about.html/', about, name='about'),
    path('gallery.html/', gallery, name='gallery'),
    path('formulario.html/', formulario, name='formulario'),
    path('API.html/', API, name='API'),
    path('register/', register, name='register'),
    path('agregar/',agregar, name='agregar'),
    path('agregarrec/',agregarrec,name='agregarrec'),
    path('eliminar/<int:id>/', eliminar,name='eliminar'),
    path('actualizar/<int:id>/',actualizar,name='actualizar'),
    path('actualizar/actualizarrec/<int:id>/',actualizarrec,name='actualizarrec')
]