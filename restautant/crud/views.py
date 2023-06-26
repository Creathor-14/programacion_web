from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect('platos/')

def plato_list(request):
    context = {'platos': Plato.objects.all()}
    return render(request,'crud/platos.html',context)

def plato_new(request):
    if request.method == 'POST':
        form = PlatoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            categoria = form.cleaned_data.get('categoria')
            precio = form.cleaned_data.get('precio')

            obj = Plato.objects.create(
                nombre = nombre,
                categoria = categoria,
                precio = precio,
            )
            obj.save()
            return redirect(reverse('platos')+ '?OK')
        else:
            return redirect(reverse('platos')+ '?FAIL')
    else:
        form = PlatoForm
    return render(request,'crud/plato-new.html',{'form':form})

def plato_update(request,plato_id):
    try:
        plato = Plato.objects.get(id = plato_id)
        form = PlatoForm(instance=plato)

        if request.method == 'POST':
            form = PlatoForm(request.POST, request.FILES, instance=videojuego)
            if form.is_valid():
                form.save()
                return redirect(reverse('videogames') + '?UPDATED')
            else:
                return redirect(reverse('videogame-edit') + videogame_id) 

        context = {'form':form}
        return render(request,'crud/videogame-edit.html',context)
    except:
        return redirect(reverse('videogames') + '?NO_EXISTS')
