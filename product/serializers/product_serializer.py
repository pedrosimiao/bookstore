from rest_framework import serializers  # Importa o módulo de serializers do Django REST Framework.

from product.models.product import Product  # Importa o modelo `Product` para ser serializado.
from product.serializers.category_serializer import CategorySerializer  
# Importa o serializador de categorias para usar dentro do produto.

# Define o serializador para o modelo `Product`.
class ProductSerializer(serializers.ModelSerializer):  
    category = CategorySerializer(required=True, many=True)  
    # Associa o serializador de categorias ao campo `category` (muitos para muitos).

    class Meta:  
        model = Product  # Especifica o modelo que será serializado.
        fields = [  
            'title',  # Campo do título do produto.
            'description',  # Campo da descrição.
            'price',  # Campo do preço.
            'active',  # Campo que indica se o produto está ativo.
            'category',  # Campo relacionado com categorias.
        ]

# Este serializador é responsável por transformar os produtos e suas categorias associadas em JSON e vice-versa.
# O uso de CategorySerializer dentro de ProductSerializer permite que os dados de categorias sejam incluídos diretamente.