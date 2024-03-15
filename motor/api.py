from motor.models import Oferta
from rest_framework import viewsets, permissions
from motor.serializers import OfertaSerializer

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OfertaSerializer