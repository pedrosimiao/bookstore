import factory  # Importa a biblioteca factory_boy para criar objetos para testes.

from product.models import Product  # Importa o modelo Product para a criação de instâncias.
from product.models import Category  # Importa o modelo Category para a criação de instâncias.

# Define a factory para o modelo Category.
class CategoryFactory(factory.django.DjangoModelFactory):  
    title = factory.Faker('pystr')  
    # Gera automaticamente uma string aleatória para o campo title.

    slug = factory.Faker('pystr')  
    # Gera automaticamente uma string aleatória para o campo slug.

    description = factory.Faker('pystr')  
    # Gera automaticamente uma string aleatória para o campo description.

    active = factory.Iterator([True, False])  
    # Alterna entre True e False ao criar instâncias para o campo active.

    class Meta:  
        model = Category  
        # Associa esta factory ao modelo Category.

# Define a factory para o modelo Product.
class ProductFactory(factory.django.DjangoModelFactory):  
    price = factory.Faker('pyint')  
    # Gera automaticamente um número inteiro aleatório para o campo price.

    title = factory.Faker('pystr')  
    # Gera automaticamente uma string aleatória para o campo title.

    category = factory.LazyAttribute(CategoryFactory)  
    # Associa uma instância gerada por CategoryFactory ao campo category.

    # Método executado após a geração de um produto.
    @factory.post_generation  
    def category(self, create, extracted, **kwargs):  
        if not create:  # Se o produto ainda não foi salvo, não faz nada.
            return
        
        if extracted:  
            # Se extracted contiver categorias passadas explicitamente, adiciona-as ao produto.
            for categories in extracted:
                self.category.add(categories)

    class Meta:  
        model = Product  
        # Associa esta factory ao modelo Product.


# Estas factories criam objetos Category e Product automaticamente para testes.
# A CategoryFactory pode gerar categorias com atributos aleatórios.
# A ProductFactory permite associar categorias ao produto e gerar produtos completos.
