import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from core.models.product import Product


@pytest.mark.django_db
def test_create_order():
    # Cria o usuário
    user = User.objects.create_user(username='testuser', password='testpass')

    # Gera o token
    token = Token.objects.create(user=user)

    # Cria produto
    product = Product.objects.create(title="Produto Teste", price=49.90, active=True)

    # Cria cliente e adiciona o token no header
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # Payload da requisição
    payload = {
        "status": "pending",
        "items": [
            {"product_id": product.id, "quantity": 2}
        ]
    }

    # Faz a requisição POST
    response = client.post("/api/orders/", payload, format='json')

    # Verificações
    assert response.status_code == 201
    assert response.data["status"] == "pending"
    assert len(response.data["items"]) == 1
