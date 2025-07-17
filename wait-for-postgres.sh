#!/bin/sh

echo "Aguardando o banco de dados aceitar conexões..."

until pg_isready -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER > /dev/null 2>&1; do
  sleep 1
done

echo "Banco de dados está pronto para receber conexões!"

