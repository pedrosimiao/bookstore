from rest_framework import (
    serializers,
)  # Importa o módulo de serializers do Django REST Framework.

from product.models.category import Category  # Importa o modelo Category.
from product.models.product import Product  # Importa o modelo Product.

from product.serializers.category_serializer import CategorySerializer

# Importa o serializador de categorias para reutilizar na serialização de campos relacionados.


class ProductSerializer(serializers.ModelSerializer):
    # Campo que utiliza o CategorySerializer para exibir os detalhes das categorias relacionadas.
    category = CategorySerializer(required=False, many=True)
    # Campo somente para escrita (write_only) que aceita IDs de categorias relacionadas.
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),  # Define o queryset como todas as categorias disponíveis.
        write_only=True,  # Indica que este campo só será usado na entrada de dados (não aparece na saída).
        many=True,  # Permite múltiplos IDs de categorias.
    )

    class Meta:
        model = Product  # Especifica o modelo associado ao serializer.
        fields = [
            "id",  # Exibe o ID do produto.
            "title",  # Exibe o título do produto.
            "description",  # Exibe a descrição do produto.
            "price",  # Exibe o preço do produto.
            "active",  # Indica se o produto está ativo ou inativo.
            "category",  # Exibe os detalhes das categorias associadas ao produto.
            "categories_id",  # Campo para entrada de IDs de categorias ao criar ou atualizar o produto.
        ]

    def create(self, validated_data):
        # Extrai a lista de IDs das categorias do `validated_data`.
        category_data = validated_data.pop("categories_id")

        # Cria o produto no banco de dados com os dados validados.
        product = Product.objects.create(**validated_data)
        # O operador ** desempacota o dicionário validated_data para transformar suas chaves
        # # (title, description, price, etc.) em argumentos nomeados
        # e os valores correspondentes são passados como argumentos para o método create().

        # Adiciona as categorias relacionadas ao produto.
        for categories in category_data:
            product.category.add(categories)

        return product  # Retorna o produto criado.


# **Resumo do ProductSerializer:**
# - `category` usa o CategorySerializer para serializar as categorias relacionadas.
# - `categories_id` aceita apenas os IDs das categorias para criar/atualizar o produto.
# - A função `create` lida com a criação de um produto e adiciona as categorias relacionadas.


# Este serializador é responsável por transformar os produtos e suas categorias associadas em JSON e vice-versa.
# O uso de CategorySerializer dentro de ProductSerializer permite que os dados de categorias sejam incluídos diretamente.
