from django.shortcuts import render, redirect

# Create your views here.

def root(request):
    return redirect('login/')

def login(request):
    return render(request,'login_app/login.html')

def register(request):
    return render(request,'login_app/register.html')