# from rest_framework import status
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer # definir serializer
    queryset = Order.objects.all() # definir queryset
    # no caso Order.objects.all é uma query default, ou uma requisição padrão
    # que retorna todos os objetos Order existentes no banco de dados.
