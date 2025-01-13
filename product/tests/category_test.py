import pytest
from product.factories import CategoryFactory
from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_category_serializer_serialization():

    category = CategoryFactory(
        title="Data Science",
        slug="data-science",
        description="Livros sobre data science e machine learning.",
        active=True
    )


    serializer = CategorySerializer(category)
    serialized_category = serializer.data


    assert serialized_category["title"] == "Data Science"
    assert serialized_category["slug"] == "data-science"
    assert serialized_category["description"] == "Livros sobre data science e machine learning."
    assert serialized_category["active"] is True
