from django import forms
from django.forms import ModelForm
from .models import *

class VideogameForm(ModelForm):
    class Meta:
        model = VideoGame
        fields = [
            'idVideogame',
            'title',
            'platform',
            'studio',
            'value',
            'stock',
            'image'
        ]
        labels = {
            'idVideogame':'ID',
            'title':'Título',
            'platform':'Plataforma',
            'studio':'Desarrollador',
            'value':'Precio Unitario',
            'stock':'Stock',
            'image':'Imagen'
        }
        widgets = {
            'idVideogame':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'platform':forms.Select(attrs={'class':'form-control'}),
            'studio':forms.TextInput(attrs={'class':'form-control'}),
            'value':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stock':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }

class PlatformForm(ModelForm):
    pass
