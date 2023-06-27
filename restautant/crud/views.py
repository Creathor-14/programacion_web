from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
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
            image = form.cleaned_data.get('image')
            obj = Plato.objects.create(
                nombre = nombre,
                categoria = categoria,
                precio = precio,
                image = image
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
            form = PlatoForm(request.POST, request.FILES, instance=plato)
            if form.is_valid():
                form.save()
                return redirect(reverse('platos') + '?UPDATED')
            else:
                return redirect(reverse('platos-edit') + plato_id) 

        context = {'form':form}
        return render(request,'crud/plato-edit.html',context)
    except:
        return redirect(reverse('platos') + '?NO_EXISTS')

def plato_detail(request, plato_id):
    try:
        plato = Plato.objects.get(id=plato_id)
        if plato:
            context = {'plato':plato}
            return render(request,'crud/plato-detail.html',context)
        else:
            return redirect(reverse('platos') + '?lala')
    except:
        return redirect(reverse('platos') + '?FAIL')
    
def plato_delete(request,plato_id):
    plato = get_object_or_404(Plato, id=plato_id)
    plato.delete()
    return redirect(reverse('platos') + '?DELETED')
    