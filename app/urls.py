from django.urls import path
from .views import index, about, gallery, formulario, API, register

urlpatterns = [
    path('', index, name='index'),
    path('about.html/', about, name='about'),
    path('gallery.html/', gallery, name='gallery'),
    path('formulario.html/', formulario, name='formulario'),
    path('API.html/', API, name='API'),
    path('register/', register, name='register')
]
