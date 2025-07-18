FROM python:3.13-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y curl build-essential libpq-dev netcat-openbsd gnupg2 lsb-release \
    && curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - \
    && echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list \
    && apt-get update \
    && apt-get install -y postgresql-client-17 \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

COPY scripts/wait-for-postgres.sh scripts/restore-db.sh /scripts/
RUN chmod +x /scripts/wait-for-postgres.sh /scripts/restore-db.sh

EXPOSE 8000

CMD ["/scripts/wait-for-postgres.sh", "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]