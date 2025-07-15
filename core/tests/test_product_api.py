import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from core.tests.factories import SuperUserFactory, CategoryFactory, UserFactory
from core.models import Product


@pytest.mark.django_db
def test_superuser_can_create_product():
    # Cria superusuário e token
    user = SuperUserFactory()
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    category = CategoryFactory()

    payload = {
        "title": "Novo Produto",
        "price": 99,
        "active": True,
        "categories_id": [category.id],
    }

    response = client.post("/api/products/", payload, format='json')

    print(response.status_code)
    print(response.data)
    assert response.status_code == 201
    assert Product.objects.filter(title="Novo Produto").exists()


@pytest.mark.django_db
def test_normal_user_cannot_create_product():
    from core.tests.factories import UserFactory

    user = UserFactory()
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    category = CategoryFactory()

    payload = {
        "title": "Produto Negado",
        "price": 99,
        "active": True,
        "categories_id": [category.id]
    }

    response = client.post("/api/products/", payload, format='json')
    print(response.status_code)
    print(response.data)

    assert response.status_code in [403, 401]

@pytest.mark.django_db
def test_normal_user_can_read_product():
    user = UserFactory()
    token = Token.objects.create(user=user)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    response = client.get("/api/products/")
    print(response.status_code)
    print(response.data)

    assert response.status_code == 200