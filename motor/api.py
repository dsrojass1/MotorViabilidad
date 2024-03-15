import random
from time import sleep
from motor.models import InformacionFinanciera, Oferta
from rest_framework import viewsets, permissions
from motor.serializers import InformacionFinancieraSerializer, OfertaSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OfertaSerializer

    @action(detail=False, methods=['post'], url_path='generar-oferta')
    def generar_oferta(self, request):
        info_financiera_data = request.data
        info_financiera_serializer = InformacionFinancieraSerializer(data=info_financiera_data)
        if info_financiera_serializer.is_valid():
            sleep(random.uniform(3, 10))
            oferta_data = {
                'monto': round(random.uniform(1000, 10000), 2),
                'tipo': random.choice(['Personal', 'Hipotecario', 'Automotriz']),
                'tasa': round(random.uniform(1.5, 10.0), 2),
                'franquicia': random.choice(['Visa', 'MasterCard', 'Amex']),
                'descripcion': 'Descripción generada aleatoriamente.'
            }

            oferta = Oferta(**oferta_data)
            oferta_serializer = OfertaSerializer(oferta)

            return Response(oferta_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(info_financiera_serializer.errors, status=status.HTTP_400_BAD_REQUEST)