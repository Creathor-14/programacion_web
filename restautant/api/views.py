from rest_framework import viewsets
from .serializer import PlatoSerializer
from crud.models import Plato

# Create your views here.

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer



