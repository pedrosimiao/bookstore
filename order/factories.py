import factory  # Importa a biblioteca factory_boy para criar objetos para testes.

from django.contrib.auth.models import (
    User,
)  # Importa o modelo User para criar usuários.

from order.models import Order  # Importa o modelo Order para criação de pedidos.


# Define a factory para o modelo User.
class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")
    # Gera automaticamente um e-mail aleatório para o usuário.

    username = factory.Faker("user_name")
    # Gera automaticamente um nome de usuário aleatório.

    class Meta:
        model = User
        # Associa esta factory ao modelo User.


# Define a factory para o modelo Order.
class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    # Usa UserFactory para associar um usuário ao pedido.

    # Método executado após a geração de um pedido.
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:  # Se o pedido ainda não foi salvo, não faz nada.
            return

        if extracted:
            # Se extracted contiver produtos passados explicitamente, adiciona-os ao pedido.
            for products in extracted:
                self.product.add(products)

    class Meta:
        model = Order
        # Associa esta factory ao modelo Order.


# A UserFactory cria objetos User para testes com e-mail e nome de usuário aleatórios.
# A OrderFactory permite criar pedidos e associar produtos gerados automaticamente ou fornecidos.
