from rest_framework import viewsets
from .serializer import PlatoSerializer
from crud.models import Plato

from crud.models import Formulario
from .serializer import ContactoSerializer

# Create your views here.

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

class ContactoListCreateView(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = ContactoSerializer