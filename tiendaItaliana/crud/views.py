from django.shortcuts import render, redirect, reverse  

from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect(videogame_list)

def videogame_list(request):
    context = {'videojuegos':VideoGame.objects.all()}
    return render(request,'crud/videogames.html',context)