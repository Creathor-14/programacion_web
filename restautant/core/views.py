from django.shortcuts import render, HttpResponse, redirect, reverse
from crud.models import *
from crud.forms import *


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

def productos(request):
    context = {
        'principales': Principal.objects.all(),
        'bebestibles': Bebestible.objects.all(),
        'postres': Postre.objects.all()
    }
    return render(request, 'core/productos.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES )
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            paterno = form.cleaned_data.get('paterno')
            materno = form.cleaned_data.get('materno')
            rut = form.cleaned_data.get('rut')
            email = form.cleaned_data.get('email')
            comentarios = form.cleaned_data.get('comentarios')
            obj= Formulario.objects.create(
                nombre=nombre,
                paterno=paterno,
                materno=materno,
                rut=rut,
                email=email,
                comentarios=comentarios
            )
            obj.save()
            # Redirigir a otra página o mostrar un mensaje de éxito
            return redirect(reverse('contacto'))         
    else:
        form = Formulario()
    
    context = {'form': form}
    return render(request, 'core/contact_form.html', context)
