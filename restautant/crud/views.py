from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def root(request):
    return redirect('principales/')

def principal_list(request):
    context = {'principales': Principal.objects.all()}
    return render(request,'crud/principales.html',context)

def principal_new(request):
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
    