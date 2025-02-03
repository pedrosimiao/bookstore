from rest_framework import (
    serializers,
)  # Importa o módulo de serializers do Django REST Framework.

from product.models import Category  # Importa o modelo `Category` para ser serializado.


# Define o serializador para o modelo `Category`.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Especifica o modelo que será usado pelo serializador.
        fields = [
            "title",  # Inclui o campo `title` no serializador.
            "slug",  # Inclui o campo `slug` no serializador.
            "description",  # Inclui o campo `description` no serializador.
            "active",  # Inclui o campo `active` no serializador.
        ]
        extra_kwargs = {"slug": {"required": False}}


# Este serializador transforma instâncias do modelo Category
# (ou consultas do banco de dados) em representações JSON para APIs e vice-versa.
