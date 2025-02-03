from django.db import models  # Importa o módulo de modelos do Django.

from product.models.category import (
    Category,
)  # Importa o modelo `Category` para criar um relacionamento.


# Define a classe `Product` que representa a tabela de produtos no banco.
class Product(models.Model):
    title = models.CharField(
        max_length=100
    )  # Define um campo de texto com limite de 100 caracteres para o título do produto. (Provavelmente há um erro de digitação aqui; o correto seria `title`).
    description = models.TextField(
        max_length=500, blank=True, null=True
    )  # Um campo de descrição opcional com até 500 caracteres.
    price = models.PositiveIntegerField(
        null=True
    )  # Um campo para o preço (valores inteiros positivos). Pode ser nulo.
    active = models.BooleanField(default=True)  # Indica se o produto está ativo.
    category = models.ManyToManyField(
        Category, blank=True
    )  # Relacionamento "muitos para muitos" com categorias, opcional.

    # Nota: O relacionamento ManyToManyField significa que um produto pode pertencer a várias categorias e vice-versa.
