from rest_framework import routers
from .api import OfertaViewSet

router = routers.DefaultRouter()

router.register('api/ofertas', OfertaViewSet, 'ofertas')

urlpatterns = router.urls
