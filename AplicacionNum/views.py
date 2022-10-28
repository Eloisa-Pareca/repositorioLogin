from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Producto

# Create your views here. (CONTROLADORES)
from .templates.forms import ProductForm


def inicio(request):
    return HttpResponse("<h2> Hello Elo :) </h2>")
def hello(request,username):
    return HttpResponse("<h2> Hello %s :) </h2>" %username)
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def nosotros(request):
    return render(request, 'nosotros.html')
def login(request): #signin
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
def register(request): #signup
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')

            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)
def cerrarsesion(request): #signout
    logout(request)
    return redirect('index')

def productos(request):
    productos = Producto.objects.all()
    context = {'producto':productos}
    print(productos)
    return render(request, 'productos.html', context)

def agregar(request):
    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/productos/')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'agregar.html', context)

def eliminar(request,product_id):
    producto = Producto.objects.get(id=product_id)
    producto.delete()
    return redirect('producto')