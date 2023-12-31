from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def root(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")

    return redirect('formularios/')

def principal_list(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    
    context = {'principales': Principal.objects.all()}
    return render(request,'crud/principales.html',context)

def principal_by_categoria(request, categoria):
    
    try:
        principales = Principal.objects.filter(categoria=categoria)
        if principales:
            context = {'principales':principales}
            return render(request,'crud/principales.html',context)
        else:
            return redirect(reverse('principales') + '?FAIL')
    except:
        return redirect(reverse('principales') + '?FAIL')

def principal_new(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    
    if request.method == 'POST':
        form = PrincipalForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            categoria = form.cleaned_data.get('categoria')
            precio = form.cleaned_data.get('precio')
            image = form.cleaned_data.get('image')
            obj = Principal.objects.create(
                nombre = nombre,
                categoria = categoria,
                precio = precio,
                image = image
            )
            obj.save()
            return redirect(reverse('principales')+ '?OK')
        else:
            return redirect(reverse('principales')+ '?FAIL')
    else:
        form = PrincipalForm
    return render(request,'crud/principal-new.html',{'form':form})

def principal_update(request,principal_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    
    try:
        principal = Principal.objects.get(id = principal_id)
        form = PrincipalForm(instance=principal)

        if request.method == 'POST':
            form = PrincipalForm(request.POST, request.FILES, instance=principal)
            if form.is_valid():
                form.save()
                return redirect(reverse('principales') + '?UPDATED')
            else:
                return redirect(reverse('principal-edit') + principal_id) 

        context = {'form':form}
        return render(request,'crud/principal-edit.html',context)
    except:
        return redirect(reverse('principales') + '?NO_EXISTS')

def principal_detail(request, principal_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    
    try:
        principal = Principal.objects.get(id=principal_id)
        if principal:
            context = {'principal':principal}
            return render(request,'crud/principal-detail.html',context)
        else:
            return redirect(reverse('principales') + '?lala')
    except:
        return redirect(reverse('principales') + '?FAIL')
    
def principal_delete(request,principal_id):
    principal = get_object_or_404(Principal, id=principal_id)
    principal.delete()
    return redirect(reverse('principales') + '?DELETED')




def postre_list(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    context = {'postres': Postre.objects.all()}
    return render(request,'crud/postres.html',context)

def postre_by_categoria(request, categoria):
    try:
        postres = Postre.objects.filter(categoria=categoria)
        if postres:
            context = {'postres':postres}
            return render(request,'crud/postres.html',context)
        else:
            return redirect(reverse('postres') + '?FAIL')
    except:
        return redirect(reverse('postres') + '?FAIL')

def postre_new(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    if request.method == 'POST':
        form = PostreForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            categoria = form.cleaned_data.get('categoria')
            precio = form.cleaned_data.get('precio')
            image = form.cleaned_data.get('image')
            obj = Postre.objects.create(
                nombre = nombre,
                categoria = categoria,
                precio = precio,
                image = image
            )
            obj.save()
            return redirect(reverse('postres')+ '?OK')
        else:
            return redirect(reverse('postres')+ '?FAIL')
    else:
        form = PostreForm
    return render(request,'crud/postre-new.html',{'form':form})

def postre_update(request,postre_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    try:
        postre = Postre.objects.get(id = postre_id)
        form = PostreForm(instance=postre)

        if request.method == 'POST':
            form = PostreForm(request.POST, request.FILES, instance=postre)
            if form.is_valid():
                form.save()
                return redirect(reverse('postres') + '?UPDATED')
            else:
                return redirect(reverse('postre-edit') + postre_id) 

        context = {'form':form}
        return render(request,'crud/postre-edit.html',context)
    except:
        return redirect(reverse('postres') + '?NO_EXISTS')

def postre_detail(request, postre_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    try:
        postre = Postre.objects.get(id=postre_id)
        if postre:
            context = {'postre':postre}
            return render(request,'crud/postre-detail.html',context)
        else:
            return redirect(reverse('postres') + '?lala')
    except:
        return redirect(reverse('postres') + '?FAIL')
    
def postre_delete(request,postre_id):
    postre = get_object_or_404(Postre, id=postre_id)
    postre.delete()
    return redirect(reverse('postres') + '?DELETED')


def bebestible_list(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    context = {'bebestibles': Bebestible.objects.all()}
    return render(request,'crud/bebestibles.html',context)

def bebestible_by_categoria(request, categoria):
    try:
        bebestibles = Bebestible.objects.filter(categoria=categoria)
        if bebestibles:
            context = {'bebestibles':bebestibles}
            return render(request,'crud/bebestibles.html',context)
        else:
            return redirect(reverse('bebestibles') + '?FAIL')
    except:
        return redirect(reverse('bebestibles') + '?FAIL')

def bebestible_new(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    
    if request.method == 'POST':
        form = BebestibleForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            categoria = form.cleaned_data.get('categoria')
            precio = form.cleaned_data.get('precio')
            image = form.cleaned_data.get('image')
            obj = Bebestible.objects.create(
                nombre = nombre,
                categoria = categoria,
                precio = precio,
                image = image
            )
            obj.save()
            return redirect(reverse('bebestibles')+ '?OK')
        else:
            return redirect(reverse('bebestibles')+ '?FAIL')
    else:
        form = BebestibleForm
    return render(request,'crud/bebestible-new.html',{'form':form})

def bebestible_update(request,bebestible_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    try:
        bebestible = Bebestible.objects.get(id = bebestible_id)
        form = BebestibleForm(instance=bebestible)

        if request.method == 'POST':
            form = BebestibleForm(request.POST, request.FILES, instance=bebestible)
            if form.is_valid():
                form.save()
                return redirect(reverse('bebestibles') + '?UPDATED')
            else:
                return redirect(reverse('bebestible-edit') + bebestible_id) 

        context = {'form':form}
        return render(request,'crud/bebestible-edit.html',context)
    except:
        return redirect(reverse('bebestibles') + '?NO_EXISTS')

def bebestible_detail(request, bebestible_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    try:
        bebestible = Bebestible.objects.get(id=bebestible_id)
        if bebestible:
            context = {'bebestible':bebestible}
            return render(request,'crud/bebestible-detail.html',context)
        else:
            return redirect(reverse('bebestibles') + '?lala')
    except:
        return redirect(reverse('bebestibles') + '?FAIL')
    
def bebestible_delete(request,bebestible_id):
    bebestible = get_object_or_404(Bebestible, id=bebestible_id)
    bebestible.delete()
    return redirect(reverse('bebestibles') + '?DELETED')
    

# Create your views here. FORMULARIO



def formulario_list(request):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    context = {'formularios': Formulario.objects.all()}
    return render(request,'crud/formularios.html',context)


def formulario_detail(request, formulario_id):
    if 'usuario' not in request.session:
        return redirect("/sesion/")
    try:
        formulario = Formulario.objects.get(id=formulario_id)
        if formulario:
            context = {'formulario':formulario}
            return render(request,'crud/formulario-detail.html',context)
        else:
            return redirect(reverse('formularios') + '?lala')
    except:
        return redirect(reverse('formularios') + '?FAIL')
    
def formulario_delete(request,formulario_id):
    formulario = get_object_or_404(Formulario, id=formulario_id)
    formulario.delete()
    return redirect(reverse('formularios') + '?DELETED')