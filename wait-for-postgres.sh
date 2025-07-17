#!/bin/sh

echo "Aguardando o banco de dados iniciar..."

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "Banco de dados iniciado!"

exec "$@"
