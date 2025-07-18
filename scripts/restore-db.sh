#!/bin/sh

set -e

echo "Iniciando restauração do banco de dados..."

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" > /dev/null 2>&1; do
  echo "Aguardando o PostgreSQL ficar pronto..."
  sleep 1
done

echo "Banco de dados está pronto. Verificando existência..."

export PGPASSWORD=$POSTGRES_PASSWORD

psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" -tc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_DB'" | grep -q 1 || \
psql -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" -c "CREATE DATABASE $POSTGRES_DB"

echo "Restaurando o dump em $POSTGRES_DB..."

pg_restore \
  --clean \
  --no-owner \
  --verbose \
  -h "$POSTGRES_HOST" \
  -p "$POSTGRES_PORT" \
  -U "$POSTGRES_USER" \
  -d "$POSTGRES_DB" \
  /app/backup.dump

echo "Restauração concluída com sucesso!"