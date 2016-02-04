from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from django.shortcuts import render_to_response


from snippets.models import Snippet, Marca, Tipo, Equipo
from snippets.serializers import MarcaSerializer, TipoSerializer, EquipoSerializer
from snippets.permissions import IsOwnerOrReadOnly

class MarcaViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

# class BuscarViewSet(viewsets.ModelViewSet):

def hello(request,pk=None):   
    if pk is None:
        return HttpResponse("Hola quien seas!")
    else:
        return HttpResponse("Hola "+pk)

   
    # def get_object(request, pk):
        
    # slpit para dividir una cadena
    # s.split(";", 1) para dividir una cadena que se separe por ; y obtener el primer resultado
    # filtrar .filter(pub_date__year=2006)

    # serializer_class = var

