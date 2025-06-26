import pytest
from rest_framework.test import APIClient
from django.urls import reverse

from product.models import Product
from product.factories import ProductFactory, CategoryFactory

@pytest.mark.django_db
def test_create_product_with_categories():
    client = APIClient()

    # Cria categorias de teste
    category1 = CategoryFactory()
    category2 = CategoryFactory()

    payload = {
        "title": "Test Product",
        "description": "A test product.",
        "price": 100,
        "active": True,
        "categories_id": [category1.id, category2.id]
    }

    url = reverse("product-list")  # isso depende do seu roteamento via router
    response = client.post(url, payload, format="json")

    # Verificações
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["price"] == payload["price"]
    assert data["active"] is True
    assert "category" in data
    assert len(data["category"]) == 2

    # Verifica se as categorias estão realmente associadas no banco
    product = Product.objects.get(id=data["id"])
    assert product.category.count() == 2
    assert set(product.category.values_list("id", flat=True)) == set([category1.id, category2.id])
