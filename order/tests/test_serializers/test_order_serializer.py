import pytest
from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers.order_serializer import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_serialization():

    book1 = ProductFactory(title="Padrões de Projetos", price=4500)
    book2 = ProductFactory(title="Construindo Chatbots com Python", price=5000)

    order = OrderFactory(product=[book1, book2])

    serializer = OrderSerializer(order)
    serialized_order = serializer.data

    assert len(serialized_order["product"]) == 2
    assert serialized_order["total"] == 9500
    assert serialized_order["product"][0]["title"] == "Padrões de Projetos"
    assert serialized_order["product"][1]["title"] == "Construindo Chatbots com Python"
