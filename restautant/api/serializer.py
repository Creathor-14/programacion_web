from rest_framework import serializers
from crud.models import Plato

from rest_framework import serializers
from crud.models import Formulario 


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        # fields = ("categoria","nombre")
        fields = '__all__'

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['nombre', 'paterno', 'materno', 'rut', 'email', 'comentarios']