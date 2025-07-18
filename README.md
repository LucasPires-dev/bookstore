# Bookstore API

API REST para gerenciar categorias e produtos de uma livraria gospel, com autenticação via token.

## Tecnologias

- Python 3.13  
- Django 5.2.4  
- Django REST Framework  
- Autenticação por Token (DRF TokenAuthentication)  
- Poetry para gerenciamento de dependências e ambiente  

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/LucasPires-dev/bookstore.git
cd bookstore
```

2. Instale o Poetry (se ainda não tiver):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Instale as dependências e crie o ambiente virtual com Poetry:

```bash
poetry install --no-root
```

4. Permita a execução dos scripts de espera do postgres (wait-for-postgres.sh) e do que populará seu banco com dados (restore-db.sh):

```bash
dos2unix scripts/*.sh        # Corrige os finais de linha se necessário
chmod +x scripts/*.sh        # Dá permissão de execução


```

5. Crie e execulte os containers da aplicação:

```bash
docker compose up --build
```

## Endpoints Principais

### Criação de conta

- `Post /api/users/register/'`

    Envie Json com as informaçoes para criação do login

    ```json
    {
        "username": "nome_de_usuario",
        "password": "senha_de_usuario",
        "email": "email_de_usuario",
        "first_name": "SEU_NOME",
        "last_name": "SEU_SOBRENOME"
    }
  ```

### Autenticação

- `POST /api/token/`

  Envie JSON com as credenciais:

  ```json
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```

  Receberá resposta com token:

  ```json
  {
    "token": "seu_token_aqui"
  }
  ```

<!-- ### Categorias

- `GET /api/categories/` - Listar categorias  
- `POST /api/categories/` - Criar categoria (somente superusuário)  
- `GET /api/categories/{id}/` - Detalhes categoria  
- `PUT/PATCH /api/categories/{id}/` - Atualizar categoria (somente superusuário)  
- `DELETE /api/categories/{id}/` - Excluir categoria (somente superusuário)   -->

### Produtos

- `GET /api/products/` - Listar produtos  
- `POST /api/products/` - Criar produto
- `GET /api/products/{id}/` - Detalhes produto  
- `PUT/PATCH /api/products/{id}/` - Atualizar produto (somente superusuário)  
- `DELETE /api/products/{id}/` - Excluir produto (somente superusuário)  

### Pedidos

- `GET /api/orders/` - Listar pedidos  
- `POST /api/orders/` - Criar pedido

body: 
```bash
{
    "status": "status_do_pedido",
    "items": [
    {"product_id": "id_do_produto1", "quantity": "quantidade_do_produto1"},
    {"product_id": "id_do_produto2", "quantity": "quantidade_do_produto2"},
    ]
}
```

- `GET /api/orders/{id}/` - Detalhes pedido  
- `PUT/PATCH /api/orders/{id}/` - Atualizar pedido (somente superusuário)  
- `DELETE /api/orders/{id}/` - Excluir pedido (somente superusuário)  

## Autorização

Para endpoints protegidos, envie o token no header da requisição:

```
Authorization: Token seu_token_aqui
```

Usuários autenticados podem apenas ler dados (GET) e eviar Pedidos (POST).  
Somente superusuários podem criar, editar ou excluir Produtos.

## Testando com Postman

1. Faça um POST para `/api/token/` com usuário e senha para obter o token.  
2. Copie o token da resposta.  
3. Nas requisições protegidas, adicione o header:

```
Authorization: Token seu_token_aqui
```

## Contribuição

Pull requests são bem-vindos! Por favor, abra uma issue antes para discutirmos alterações significativas.

