from django.shortcuts import render, redirect
from .models import Alumno

# Create your views here.
def index(request):
    alu=Alumno.objects.all()
    return render(request,'index.html',{'alu':alu})

def agregar(request):
    return render(request, 'agregar.html')

def agregarrec(request):
    x=request.POST['nombre']
    y=request.POST['apellido']
    z=request.POST['comuna']
    alu=Alumno(nombre=x,apellido=y,comuna=z)
    alu.save()
    return redirect("/")