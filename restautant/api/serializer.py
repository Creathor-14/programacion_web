from rest_framework import serializers
from crud.models import Principal

from rest_framework import serializers
from crud.models import Formulario 


class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        # fields = ("categoria","nombre")
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['nombre', 'paterno', 'materno', 'rut', 'email', 'comentarios']