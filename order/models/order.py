from django.db import models  # Importa o módulo de modelos do Django.
from django.contrib.auth.models import User  # Importa o modelo de usuários padrão do Django.

from product.models.product import Product  # Importa o modelo `Product` para criar um relacionamento.

# Define a classe `Order` que representa pedidos no sistema.
class Order(models.Model):  
    product = models.ManyToManyField(Product, blank=False)  # Relacionamento "muitos para muitos" com produtos (obrigatório).
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)  
    # Relacionamento "um para muitos" com usuários. Se o usuário for deletado, o pedido será excluído (on_delete=models.CASCADE).
