from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from snippets.models import Marca, Tipo, Equipo
from django.contrib.auth.models import User




class MarcaSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Marca
        fields = ('__all__')


class TipoSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Tipo
        fields = ('__all__')


class EquipoSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Equipo
        fields = ('__all__')