import pytest
from product.factories import ProductFactory
from product.models import Product


@pytest.mark.django_db
def test_product_creation():
    product = ProductFactory()

    assert isinstance(product, Product)
    assert product.title is not None
    assert product.price is not None
    assert product.category.count() > 0

    category = product.category.first()
    assert category is not None
    assert category.title is not None
