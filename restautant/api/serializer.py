from rest_framework import serializers
from crud.models import Plato

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        # fields = ("categoria","nombre")
        fields = '__all__'