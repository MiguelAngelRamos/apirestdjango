from rest_framework.routers import  DefaultRouter
from clientes.api.views import ClienteApiViewSet

router_clientes = DefaultRouter()
router_clientes.register(prefix='clientes', basename='clientes', viewset=ClienteApiViewSet)