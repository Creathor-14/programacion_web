from rest_framework import serializers
from crud.models import * 


class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        # fields = ("categoria","nombre")
        fields = (
            'id',
            'nombre',
            'categoria',
            'precio'
        )

class PostreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postre
        fields = (
            'id',
            'nombre',
            'categoria',
            'precio'
        )

class BebestibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bebestible
        # fields = ("categoria","nombre")
        fields = (
            'id',
            'nombre',
            'categoria',
            'precio'
        )

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['nombre', 'paterno', 'materno', 'rut', 'email', 'comentarios']