from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from clientes.models import Cliente
from clientes.api.serializers import ClienteSerializer
from clientes.api.permissions import IsAdminOrReadOnly

class ClienteApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    #queryset = Cliente.objects.filter(activo=True)
    #lookup_field = 'slug' # que ahora en vez de id use el slug para buscar
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['activo', 'name']

