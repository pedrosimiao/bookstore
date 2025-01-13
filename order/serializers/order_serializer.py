from rest_framework import serializers  # Importa o módulo de serializers do Django REST Framework.

from order.models.order import Order

from product.serializers import ProductSerializer  
# Importa o serializador de produtos para ser usado na associação.

# Define o serializador para o modelo `Order`.
class OrderSerializer(serializers.ModelSerializer):  
    product = ProductSerializer(required=True, many=True)  
    # Usa o serializador de produtos para o campo `product` (muitos para muitos).

    total = serializers.SerializerMethodField()  
    # Define um campo calculado para o total.

    # Método para calcular o total.
    def get_total(self, instance):  
        total = sum([product.price for product in instance.product.all()])  
        # Soma o preço de todos os produtos associados ao pedido.
        return total  

    class Meta:  
        model = Order  # Especifica o modelo associado.
        fields = [  
            'product',  # Inclui os produtos no pedido.
            'total',  # Inclui o total calculado.
        ]

# Este serializador lida com pedidos e produtos relacionados.
# O campo total é calculado dinamicamente com base nos produtos do pedido.