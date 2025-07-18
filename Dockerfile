FROM python:3.13-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema
RUN apt-get update \
    && apt-get install -y curl build-essential libpq-dev netcat-openbsd gnupg2 lsb-release \
    && curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && apt-get update \
    && apt-get install -y postgresql-client-17 \
    && apt-get clean

# Instala o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Define o diretório de trabalho
WORKDIR /app

# Copia arquivos essenciais para instalação
COPY pyproject.toml poetry.lock* /app/

# Instala dependências via Poetry (sem criar venv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copia o restante do projeto
COPY . .

# Copia scripts separadamente para evitar conflito com volume montado
COPY scripts/wait-for-postgres.sh scripts/restore-db.sh /scripts/
RUN chmod +x /scripts/wait-for-postgres.sh /scripts/restore-db.sh

EXPOSE 8000

# Usa o script de espera + restore + runserver
CMD ["/scripts/wait-for-postgres.sh", "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
