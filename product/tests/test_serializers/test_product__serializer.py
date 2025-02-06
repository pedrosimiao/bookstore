import pytest
from product.factories import ProductFactory, CategoryFactory
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer_serialization():

    category_1 = CategoryFactory(title="Programming")
    category_2 = CategoryFactory(title="Software Development")

    book = ProductFactory(
        title="React Fluente", category=[category_1, category_2], price=6000
    )

    serializer = ProductSerializer(book)
    serialized_book = serializer.data

    assert serialized_book["title"] == "React Fluente"
    assert serialized_book["price"] == 6000
    assert len(serialized_book["category"]) == 2
    assert serialized_book["category"][0]["title"] == "Programming"
    assert serialized_book["category"][1]["title"] == "Software Development"
