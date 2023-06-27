from crud.models import *
from .serializer import *


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

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

@api_view(['GET','POST','DELETE'])
def principal_list(request):
    if request.method == 'GET':#funcionando /?nombre=api
        principales = Principal.objects.all()

        nombre = request.query_params.get('nombre',None)
        if nombre is not None:
            principales = principales.filter(nombre__contains=nombre)

        categoria = request.query_params.get('categoria',None)
        if categoria is not None:
            principales = principales.filter(categoria__contains=categoria)

        precio = request.query_params.get('precio',None)
        if precio is not None:
            principales = principales.filter(precio__contains=precio)

        principal_serializer = PrincipalSerializer(principales,many=True)
        return Response(principal_serializer.data)
    
    elif request.method == 'POST':#funcionando
        principal_data = JSONParser().parse(request)
        principal_serializer = PrincipalSerializer(data=principal_data)
        if principal_serializer.is_valid():
            principal_serializer.save()
            return JsonResponse(principal_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(principal_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':#funcionando
        cantidad = Principal.objects.all().delete()
        return Response({'mensaje':'Se han eliminado {} principales de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT','DELETE'])
def principal_detail(request,principal_id):
    try:
        principal = Principal.objects.get(id=principal_id)
    except:
        return Response({'mensaje':'El principal {} no existe en nuestros registros'.format(principal_id)},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':#funcionando
        principal_serializer = PrincipalSerializer(principal)
        return Response(principal_serializer.data)
    
    elif request.method == 'PUT':#funcionando
        principal_data = JSONParser().parse(request)
        principal_serializer = PrincipalSerializer(principal, data=principal_data)
        if principal_serializer.is_valid():
            principal_serializer.save()
            return JsonResponse(principal_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(principal_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':#funcionando
        principal.delete()
        return Response({'mensaje':'El principal {} ha sido eliminado de la base de datos.'.format(principal_id)},status=status.HTTP_204_NO_CONTENT)