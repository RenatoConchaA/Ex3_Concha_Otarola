from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto

# Create your views here.
def index(request):
    return render(request,'app/index.html')

def about(request):
    return render(request,'app/about.html')

@login_required
def gallery(request):
    return render(request,'app/gallery.html')

def formulario(request):
    return render(request,'app/formulario.html')

def API(request):
    return render(request,'app/API.html')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('index')
    return render(request, 'registration/register.html',data)

def index_2(request):
    alu=Producto.objects.all()
    return render(request,'index.html',{'alu':alu})

def agregar(request):
    return render(request, 'agregar.html')

def agregarrec(request):
    x=request.POST['Producto']
    y=request.POST['Descripcion']
    z=request.POST['Precio']
    alu=Producto(Producto=x,Descripcion=y,Precio=z)
    alu.save()
    return redirect("/")

def eliminar(request,id):
    alu=Producto.objects.get(id=id)
    alu.delete()
    return redirect("/")

def actualizar(request,id):
    alu=Producto.objects.get(id=id)
    return render(request,'actualizar.html',{'alu':alu})

def actualizarrec(request,id):
    x=request.POST['Producto']
    y=request.POST['Descripcion']
    z=request.POST['Precio']
    alu=Producto.objects.get(id=id)
    alu.producto=x
    alu.descripcion=y
    alu.precio=z
    alu.save()
    return redirect("/")