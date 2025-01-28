from rest_framework import serializers  # Importa o módulo de serializers do Django REST Framework.

from order.models.order import Order  # Importa o modelo Order.
from product.models.product import Product  # Importa o modelo Product.

from product.serializers import ProductSerializer  
# Importa o serializador de produtos para reutilizar na serialização de campos relacionados.

class OrderSerializer(serializers.ModelSerializer):  
    # Campo que utiliza o ProductSerializer para exibir os detalhes dos produtos relacionados.
    product = ProductSerializer(read_only=True, many=True)  
    # Campo somente para escrita (write_only) que aceita IDs de produtos relacionados.
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),  # Define o queryset como todos os produtos disponíveis.
        write_only=True,  # Indica que este campo só será usado na entrada de dados (não aparece na saída).
        many=True  # Permite múltiplos IDs de produtos.
    )
    # Campo calculado que retorna o valor total do pedido.
    total = serializers.SerializerMethodField()  

    # Método para calcular o valor total do pedido.
    def get_total(self, instance):  
        # Soma o preço de todos os produtos associados ao pedido.
        total = sum([product.price for product in instance.product.all()])  
        return total  # Retorna o valor total calculado.

    class Meta:  
        model = Order  # Especifica o modelo associado ao serializer.
        fields = [  
            'product',  # Exibe os detalhes dos produtos associados ao pedido.
            'total',  # Exibe o valor total calculado.
            'user',  # Exibe o usuário associado ao pedido.
            'products_id'  # Campo para entrada de IDs de produtos ao criar ou atualizar o pedido.
        ]
        # Define que o campo `product` não é obrigatório na entrada de dados.
        extra_kwargs = {'product': {'required': False}}

    def create(self, validated_data):
        # Extrai a lista de IDs dos produtos do `validated_data`.
        product_data = validated_data.pop('products_id')  
        # Extrai o usuário do `validated_data`.
        user_data = validated_data.pop('user')  

        # Cria o pedido no banco de dados.
        order = Order.objects.create(user=user_data)  
        # O operador ** desempacota o dicionário validated_data para transformar suas chaves
        # # (title, description, price, etc.) em argumentos nomeados
        # e os valores correspondentes são passados como argumentos para o método create().
        
        # Adiciona os produtos relacionados ao pedido.
        for product in product_data:
            order.product.add(product)  

        return order  # Retorna o pedido criado.

# **Resumo do OrderSerializer:**
# - `product` usa o ProductSerializer para serializar os produtos relacionados.
# - `products_id` aceita apenas os IDs dos produtos para criar/atualizar o pedido.
# - O campo `total` é calculado dinamicamente com base nos preços dos produtos associados.
# - A função `create` lida com a criação de um pedido e adiciona os produtos relacionados.


# Este serializador lida com pedidos e produtos relacionados.
# O campo total é calculado dinamicamente com base nos produtos do pedido.