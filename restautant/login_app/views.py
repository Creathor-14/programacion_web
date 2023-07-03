from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
import bcrypt
# Create your views here.

def root(request):
    return redirect('login/')

def login(request):
    return render(request,'login_app/login.html')

#def register(request):
#    return render(request,'login_app/register.html')

def register(request):
    if request.method == 'GET':
        return render(request,'login_app/register.html')
    else:
        if request.method == 'POST':
            print("llege")
            errors = Usuario.objects.validador_campos(request.POST)

            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)

                #Si se produce un error pero no queremos perder los datos....
                request.session['registro_nombre'] = request.POST['nombre']
                request.session['registro_apellido'] = request.POST['apellido']
                request.session['registro_email'] = request.POST['email']
                request.session['level_mensaje'] = 'alert-danger'

            else:
                request.session['registro_nombre'] = ""
                request.session['registro_apellido'] = ""
                request.session['registro_email'] = ""

                nombre = request.POST['nombre']
                apellido = request.POST['apellido']
                email = request.POST['email']
                clave_hash = bcrypt.hashpw(request.POST['clave'].encode(), bcrypt.gensalt()).decode()

                obj = Usuario.objects.create(nombre=nombre, apellido=apellido,email=email,clave=clave_hash)
                messages.success(request, "Usuario registrado con éxito!!!!")
                request.session['level_mensaje'] = 'alert-success'
            
            return render(request,'login_app/login.html')

        return render(request, 'login_app/login.html')