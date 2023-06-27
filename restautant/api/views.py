from crud.models import *
from .serializer import *


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

# Create your views here.


class ContactoListCreateView(viewsets.ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = ContactoSerializer

@api_view(['GET','POST','DELETE'])
def principal_list(request):
    print("yeee")
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
        print("hahahahah123")
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
    
#----------------------------------------------------------------------------    
#----------------------------------------------------------------------------    
#----------------------------------------------------------------------------    
@api_view(['GET','POST','DELETE'])
def postre_list(request):
    if request.method == 'GET':#funcionando /?nombre=api
        postres = Postre.objects.all()

        nombre = request.query_params.get('nombre',None)
        if nombre is not None:
            postres = postres.filter(nombre__contains=nombre)

        categoria = request.query_params.get('categoria',None)
        if categoria is not None:
            postres = postres.filter(categoria__contains=categoria)

        precio = request.query_params.get('precio',None)
        if precio is not None:
            postres = postres.filter(precio__contains=precio)

        postre_serializer = PostreSerializer(postres,many=True)
        return Response(postre_serializer.data)
    
    elif request.method == 'POST':#funcionando
        postre_data = JSONParser().parse(request)
        postre_serializer = PostreSerializer(data=postre_data)
        if postre_serializer.is_valid():
            postre_serializer.save()
            return JsonResponse(postre_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(postre_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':#funcionando
        cantidad = Postre.objects.all().delete()
        return Response({'mensaje':'Se han eliminado {} postres de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT','DELETE'])
def postre_detail(request,postre_id):
    try:
        postre = Postre.objects.get(id=postre_id)
    except:
        return Response({'mensaje':'El postre {} no existe en nuestros registros'.format(postre_id)},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':#funcionando
        postre_serializer = PostreSerializer(postre)
        return Response(postre_serializer.data)
    
    elif request.method == 'PUT':#funcionando
        postre_data = JSONParser().parse(request)
        postre_serializer = PostreSerializer(postre, data=postre_data)
        if postre_serializer.is_valid():
            postre_serializer.save()
            return JsonResponse(postre_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(postre_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':#funcionando
        postre.delete()
        return Response({'mensaje':'El postre {} ha sido eliminado de la base de datos.'.format(postre_id)},status=status.HTTP_204_NO_CONTENT)

        
#----------------------------------------------------------------------------    
#----------------------------------------------------------------------------    
#----------------------------------------------------------------------------    

@api_view(['GET','POST','DELETE'])
def bebestible_list(request):
    if request.method == 'GET':#funcionando /?nombre=api
        bebestibles = Bebestible.objects.all()

        nombre = request.query_params.get('nombre',None)
        if nombre is not None:
            bebestibles = bebestibles.filter(nombre__contains=nombre)

        categoria = request.query_params.get('categoria',None)
        if categoria is not None:
            bebestibles = bebestibles.filter(categoria__contains=categoria)

        precio = request.query_params.get('precio',None)
        if precio is not None:
            bebestibles = bebestibles.filter(precio__contains=precio)

        bebestible_serializer = BebestibleSerializer(bebestibles,many=True)
        return Response(bebestible_serializer.data)
    
    elif request.method == 'POST':#funcionando
        bebestible_data = JSONParser().parse(request)
        bebestible_serializer = BebestibleSerializer(data=bebestible_data)
        if bebestible_serializer.is_valid():
            bebestible_serializer.save()
            return JsonResponse(bebestible_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(bebestible_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':#funcionando
        cantidad = Bebestible.objects.all().delete()
        return Response({'mensaje':'Se han eliminado {} bebestibles de la base de datos.'.format(cantidad[0])},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','PUT','DELETE'])
def bebestible_detail(request,bebestible_id):
    try:
        bebestible = Bebestible.objects.get(id=bebestible_id)
    except:
        return Response({'mensaje':'El bebestible {} no existe en nuestros registros'.format(bebestible_id)},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':#funcionando
        bebestible_serializer = BebestibleSerializer(bebestible)
        return Response(bebestible_serializer.data)
    
    elif request.method == 'PUT':#funcionando
        bebestible_data = JSONParser().parse(request)
        bebestible_serializer = BebestibleSerializer(bebestible, data=bebestible_data)
        if bebestible_serializer.is_valid():
            bebestible_serializer.save()
            return JsonResponse(bebestible_serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(bebestible_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':#funcionando
        bebestible.delete()
        return Response({'mensaje':'El bebestible {} ha sido eliminado de la base de datos.'.format(bebestible_id)},status=status.HTTP_204_NO_CONTENT)
