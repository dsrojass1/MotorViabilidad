from rest_framework import serializers
from .models import InformacionFinanciera, Oferta

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        exclude = ['id', ]

class InformacionFinancieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionFinanciera
        fields = '__all__'
        read_only_fields = ['id', ]