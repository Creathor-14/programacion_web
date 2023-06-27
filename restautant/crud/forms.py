from django import forms
from django.forms import ModelForm
from .models import *

class FormularioForm(ModelForm):
    class Meta:
        model = Formulario
        fields = [
            'nombre',
            'paterno',
            'materno',
            'rut',
            'email',
            'comentarios'
        ]
        labels = {
            'nombre' : 'Nombre', 
            'paterno': 'Paterno',
            'materno': 'Materno',
            'rut': 'Rut',
            'email': 'Email',
            'comentarios': 'Comentarios'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'paterno':forms.TextInput(attrs={'class':'form-control'}),
            'materno':forms.TextInput(attrs={'class':'form-control'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'comentarios':forms.TextInput(attrs={'class':'form-control'})
        }
class PrincipalForm(ModelForm):
    class Meta:
        model = Principal
        fields = [
            'nombre',
            'categoria',
            'precio',
            'image'
        ]
        labels = {
            'nombre' : 'Nombre', 
            'categoria': 'Categoria',
            'precio': 'Precio',
            'image':'Imagen'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }


class PostreForm(ModelForm):
    class Meta:
        model = Postre
        fields = [
            'nombre',
            'categoria',
            'precio',
            'image'
        ]
        labels = {
            'nombre' : 'Nombre', 
            'categoria': 'Categoria',
            'precio': 'Precio',
            'image':'Imagen'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class BebestibleForm(ModelForm):
    class Meta:
        model = Bebestible
        fields = [
            'nombre',
            'categoria',
            'precio',
            'image'
        ]
        labels = {
            'nombre' : 'Nombre', 
            'categoria': 'Categoria',
            'precio': 'Precio',
            'image':'Imagen'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.TextInput(attrs={'class':'form-control'}),
            'precio':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }
