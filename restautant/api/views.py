from rest_framework import viewsets
from crud.models import Principal

from crud.models import Formulario
from .serializer import *

# Create your views here.

class PrincipalViewSet(viewsets.ModelViewSet):
    queryset = Principal.objects.all()
    serializer_class = PrincipalSerializer

class PostreViewSet(viewsets.ModelViewSet):
    queryset = Postre.objects.all()
    serializer_class = PostreSerializer

class BebestibleViewSet(viewsets.ModelViewSet):
    queryset = Bebestible.objects.all()
    serializer_class = BebestibleSerializer

class ContactoListCreateView(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = ContactoSerializer