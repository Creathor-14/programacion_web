from django.shortcuts import render, HttpResponse, redirect
from crud.models import *

# Create your views here.
def root(request):
    return redirect('home')

def home(request):
    return render(request,'core/home.html')

def contacto(request):
    return render(request,'core/contacto.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def historia(request):
    return render(request,'core/historia.html')

def chistes(request):
    return render(request,'core/chistes.html')

