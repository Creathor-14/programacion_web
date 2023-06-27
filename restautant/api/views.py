from rest_framework import viewsets
from .serializer import PrincipalSerializer
from crud.models import Principal

from crud.models import Formulario
from .serializer import ContactoSerializer

# Create your views here.

class PrincipalViewSet(viewsets.ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer

class ContactoListCreateView(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = ContactoSerializer