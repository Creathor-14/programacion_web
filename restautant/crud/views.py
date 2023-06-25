from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect('platos/')

def plato_list(request):
    context = {'platos': Plato.objects.all()}
    return render(request,'crud/platos.html',context)
