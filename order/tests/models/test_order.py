import pytest

from order.factories import OrderFactory
from product.factories import ProductFactory


@pytest.mark.django_db
def test_order_creation_with_products():
    product1 = ProductFactory()
    product2 = ProductFactory()

    order = OrderFactory(product=[product1, product2])

    assert order.product.count() == 2